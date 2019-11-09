#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QInputDialog, QMessageBox
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen, QPixmap, QMouseEvent, QPaintEvent
from PIL import Image

from fonctions.angleToFunction import angleToFunction
from fonctions.functionIntersect import functionIntersect
from fonctions.WGS84DecToDeg import WGS84DecToDeg
from fonctions.WGS84DegToDec import WGS84DegToDec
from uiFunctions import *


class DrawMap(QWidget):
    def __init__(self, im, parentClass):
        super().__init__()
        self.parentClass = parentClass
        self.line = []
        self.fx = []
        self.intersect = ()
        self.gps = ()
        self.ndDec, self.wdDec, self.westDec, self.nordDec = None, None, None, None
        self.im = im
        self.mode = "amer"
        image = Image.open(im)
        self.imSize = image.size
        self.setMinimumWidth(image.size[0])
        self.setMinimumHeight(image.size[1])
        self.setMaximumWidth(image.size[0])
        self.setMaximumHeight(image.size[1])
        # self.init_ui()

    def supprimerTraces(self):
        """supprime le tracé des amers"""
        self.line = []
        self.fx = []
        self.intersect = ()
        self.westDec, self.nordDec = None, None
        self.parentClass.updateLabelsAmer("→", "→")
        self.update()

    def paintEvent(self, event):
        """
        impressions des formes sur la carte
            @type event: QPaintEvent
        """
        painter = QPainter(self)
        pixmap = QPixmap(self.im)
        painter.drawPixmap(self.rect(), pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        pen = QPen(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)
        for line in self.line:
            painter.drawLine(*line)
        if self.intersect:
            pen.setColor(Qt.blue)
            painter.setPen(pen)
            painter.drawEllipse(abs(self.intersect[0]) - 5, abs(self.intersect[1]) - 5, 10, 10)
        if self.gps:
            pen.setColor(Qt.red)
            painter.setPen(pen)
            painter.drawEllipse(self.gps[0] - 5, self.gps[1] - 5, 10, 10)
        return

    def amerCreation(self, event):
        """
        Creation du trace des amers et determination de la position
            @type event: QMouseEvent
            @param event: objet clic de souris
        """
        pos = event.pos()
        # fenetre demande angle de l'amer
        deg, ok = QInputDialog.getDouble(self, "Angle de l'amer", "Angle de l'amer")
        # si click ok
        if ok:
            # si angle valide
            if 0. <= deg < 360.:
                # supprime les anciens traces
                if len(self.line) > 2:
                    self.supprimerTraces()
                # cas 0 et 180
                if deg == 0:
                    # self.line.append((pos.x(), 0, pos.x(), pos.y()))
                    # recalcule de a,b pour eviter le cas x=n
                    # la perte de la précision est negligeable dans notre cas ou l'echelle et la carte est petite
                    deg = deg + 10e-8

                elif deg == 180:
                    # self.line.append((pos.x(), self.imSize[1], pos.x(), pos.y()))
                    # recalcule de a,b pour eviter le cas x=n
                    # la perte de la précision est negligeable dans notre cas ou l'echelle et la carte est petite
                    deg = deg + 10e-8

                # calcul de la fonction de la droite
                a, b = angleToFunction(deg, (pos.x(), pos.y()))
                # print("ab", a, b)
                # test des cas pour la direction
                if deg < 180:
                    y2 = -a * 1650 + b
                    x2 = 1650
                else:
                    y2 = a * 1650 + b
                    x2 = -1650
                    # evite l'overflow du GUI
                if y2 > 2147483647:
                    y2 = 2147483646
                elif y2 < -2147483648:
                    y2 = -2147483648

                self.fx.append((-a, b))
                self.line.append((pos.x(), pos.y(), x2, y2))

                # si 2 doites => calcul de l'intersection
                if len(self.fx) == 2:
                    # print("calcul du pt")
                    try:
                        pt = functionIntersect(*self.fx[0], *self.fx[1])
                    except:
                        QMessageBox.critical(self, "Amer invalide", "deux amers différents sont requis")
                        self.supprimerTraces()
                        return
                    # conversion en pixel => degree decimal
                    self.westDec = 3.0 - (pt[0] * -0.000342936)
                    self.nordDec = 47.519635 + pt[1] * -0.000232025
                    # conversion en degrée
                    nordDeg = WGS84DecToDeg(self.nordDec)
                    westDeg = WGS84DecToDeg(self.westDec)
                    self.parentClass.updateLabelsAmer("{}° {}' {}\"N".format(*nordDeg),
                                                      "{}° {}' {}\"W".format(*westDeg))
                    self.intersect = pt
                    self.computeAmerGPSError()

            # sinon angle invalide
            else:
                # Warning box angle invalide
                QMessageBox.critical(self, "Angle invalide", "l'angle doit être entre 0 et 360°")

        self.update()


    def gpsDialogManager(self):
        """
        Hook pour la fenetre de dialogue GPS
        """
        dlg = GpsDialog(self)
        if dlg.exec_():
            pass
            # print("Success!")
        # else:
        #    print("Cancel!")


    def getGpsCoordinates(self, ncord, wcord):
        """
        Affiche le point GPS sur la carte
        @type Ncord: tuple
        @param Ncord: Cordonée sexadecimal Nord
        @type Wcord: tuple
        @param Wcord: Cordonée sexadecimal ouest
        """
        self.parentClass.updateLabelsGPS("{}° {}' {}\"N".format(*ncord),
                                         "{}° {}' {}\"W".format(*wcord))
        self.ndDec = WGS84DegToDec(*ncord)
        self.wdDec = WGS84DegToDec(*wcord)
        # print(ndDec, wdDec)
        xcoord = abs((self.wdDec - 3.0) / 0.000342936)
        ycoord = abs((self.ndDec - 47.519635) / -0.000232025)
        self.gps = (xcoord, ycoord)
        self.update()
        self.computeAmerGPSError()
        # print(xcoord, ycoord)


    def computeAmerGPSError(self):
        """
        Calcul l'erreur entre le relevé des amers et la position GPS
        """
        if self.ndDec and self.wdDec and self.nordDec and self.westDec:
            ndelta = self.ndDec - self.nordDec
            wdelta = self.wdDec - self.westDec
            ndelta = WGS84DecToDeg(ndelta)
            wdelta = WGS84DecToDeg(wdelta)
            self.parentClass.updateLabelsError("{}° {}' {}\"N".format(*ndelta),
                                               "{}° {}' {}\"W".format(*wdelta))


    def mousePressEvent(self, event):
        """
        Hook evenement clic de souris
            @type event: QMouseEvent
            @param event: objet clic de souris
        """
        if self.mode == "amer":
            self.amerCreation(event)
