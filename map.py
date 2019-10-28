#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QInputDialog, QMessageBox
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen, QPixmap, QMouseEvent, QPaintEvent
from PIL import Image
from math import *

from fonctions.angleToFunction import angleToFunction
from fonctions.functionIntersect import functionIntersect


class DrawMap(QWidget):
    def __init__(self, im):
        super().__init__()
        self.line = []
        self.fx = []
        self.intersect = ()
        self.im = im
        self.mode = "amer"
        image = Image.open(im)
        self.imSize = image.size
        self.setMinimumWidth(image.size[0])
        self.setMinimumHeight(image.size[1])
        # self.init_ui()

    def supprimerTraces(self):
        """supprime le tracé des amers"""
        self.line = []
        self.fx = []
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
            # print("here", line)
            painter.drawLine(*line)
        if self.intersect:
            pen.setColor(Qt.blue)
            painter.setPen(pen)
            painter.drawEllipse(self.intersect[0] - 5, self.intersect[1] - 5, 10, 10)
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
                    self.line.append((pos.x(), 0, pos.x(), pos.y()))
                    # recalcule de a,b pour eviter le cas x=n
                    # la perte de la précision est negligeable dans notre cas ou l'echelle et la carte est petite
                    a, b = angleToFunction(deg + 10e-6, (pos.x(), pos.y()))
                    self.fx.append((a, b))
                    self.update()
                elif deg == 180:
                    self.line.append((pos.x(), self.imSize[1], pos.x(), pos.y()))
                    a, b = angleToFunction(deg + 10e-6, (pos.x(), pos.y()))
                    # recalcule de a,b pour eviter le cas x=n
                    # la perte de la précision est negligeable dans notre cas ou l'echelle et la carte est petite
                    self.fx.append((a, b))
                    self.update()
                # autres cas
                else:
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
                        QMessageBox.critical(self, "Amer invalide", "deux amer différents sont requis")
                        self.supprimerTraces()
                        return
                    # print("intersect", pt)
                    self.intersect = pt

            # sinon angle invalide
            else:
                # Warning box angle invalide
                QMessageBox.critical(self, "Angle invalide", "l'angle doit être entre 0 et 360°")

        self.update()

    def mousePressEvent(self, event):
        """
        Hook evenement clic de souris
            @type event: QMouseEvent
            @param event: objet clic de souris
        """
        if self.mode == "amer":
            self.amerCreation(event)
