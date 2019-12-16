#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAction, qApp, QMainWindow, QStyle, QDockWidget, QVBoxLayout, \
    QPushButton, QGroupBox
from PyQt5.QtGui import QIcon, QStyleHints

from map import *


class Window(QMainWindow):
    """
    Classe principale du GUI
    @author: Maxime Favier
    """
    def __init__(self):
        super().__init__()
        self.title = "Boat buddy"
        self.lblAmer1, self.lblAmer2, self.lblGPS1, self.lblGPS2, self.routeFond = None, None, None, None, None
        self.lblMaree1, self.lblMaree2, self.lblError1, self.lblError2 = None, None, None, None
        self.capCompas, self.routeSurface = None, None
        self.centralWidg = DrawMap("./maps/baie_de_quiberon.png", self)
        self.init_ui()

    def init_ui(self):
        """definitions des proprietés du GUI"""
        self.setWindowIcon(QIcon("./icons/sailboat.png"))
        self.setWindowTitle(self.title)
        self.draw_toolbar()
        self.draw_map()
        self.draw_dock()
        self.show()

    def draw_toolbar(self):
        """Creation des bouttons de la barre de tache"""
        exitAct = QAction(self.style().standardIcon(QStyle.SP_DialogCloseButton), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        #positionTool = QAction(QIcon("./icons/star.png"), "Position Tool", self)
        #positionTool.setToolTip('Calcule la position')
        delPositionTool = QAction(QIcon("./icons/delStar.png"), "Position Tool", self)
        delPositionTool.setToolTip('Supprime le tracé des amer')
        delPositionTool.triggered.connect(self.centralWidg.supprimerTraces)
        gpsTool = QAction(QIcon("./icons/satellite.png"), "GPS", self)
        gpsTool.setToolTip("Entrer une position GPS")
        gpsTool.triggered.connect(self.centralWidg.gpsDialogManager)

        mareeTool = QAction(QIcon("./icons/maree.png"), "Maree Option", self)
        mareeTool.setToolTip("Calcul de la marée")
        mareeTool.triggered.connect(self.centralWidg.mareeDialogManager)

        posTheo = QAction(QIcon("./icons/simulation"), "Position  Théorique", self)
        posTheo.setToolTip("Calcul de la position Theorique")
        posTheo.triggered.connect(self.centralWidg.posTheoriqueDialogManager)

        capCompas = QAction(QIcon("./icons/cap_compas.png"), "Cap Compas", self)
        capCompas.setToolTip("Calcul du Cap compas")
        capCompas.triggered.connect(self.centralWidg.capTheoriqueManager)


        self.toolbar = self.addToolBar('Exit')
        #self.toolbar.addAction(positionTool)
        self.toolbar.addAction(delPositionTool)
        self.toolbar.addAction(gpsTool)
        self.toolbar.addAction(mareeTool)
        self.toolbar.addAction(posTheo)
        self.toolbar.addAction(capCompas)
        self.toolbar.addAction(exitAct)

    def draw_map(self):
        """positionement de la carte"""
        self.setCentralWidget(self.centralWidg)

    def draw_dock(self):
        """Initialisation du dock"""
        self.docked = QDockWidget("", self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.docked)
        self.dockedWidget = QWidget(self)
        self.docked.setWidget(self.dockedWidget)
        self.dockedWidget.setLayout(QVBoxLayout())
        self.dockedWidget.layout().addWidget(self.groupePosition())
        self.dockedWidget.layout().addWidget(self.groupeGPS())
        self.dockedWidget.layout().addWidget(self.groupeAmersError())
        self.dockedWidget.layout().addWidget(self.groupeMaree())
        self.dockedWidget.layout().addWidget(self.groupeCap())

    def groupePosition(self):
        """Initialisation des widgets du groupe position du bateau - Amers """
        groupe = QGroupBox("Position du bateau : Amers")
        self.lblAmer1 = QLabel("→")
        self.lblAmer2 = QLabel("→")
        vbox = QVBoxLayout()
        vbox.addWidget(self.lblAmer1)
        vbox.addWidget(self.lblAmer2)
        vbox.addStretch(0)
        groupe.setLayout(vbox)
        return groupe

    def groupeGPS(self):
        """Initialisation des widgets du groupe GPS"""
        groupe = QGroupBox("Position GPS")
        self.lblGPS1 = QLabel("→")
        self.lblGPS2 = QLabel("→")
        vbox = QVBoxLayout()
        vbox.addWidget(self.lblGPS1)
        vbox.addWidget(self.lblGPS2)
        vbox.addStretch(0)
        groupe.setLayout(vbox)
        return groupe

    def groupeAmersError(self):
        """Initialisation des widgets du groupe erreur amers"""
        groupe = QGroupBox("Erreur amers / GPS")
        self.lblError1 = QLabel("→")
        self.lblError2 = QLabel("→")
        vbox = QVBoxLayout()
        vbox.addWidget(self.lblError1)
        vbox.addWidget(self.lblError2)
        vbox.addStretch(0)
        groupe.setLayout(vbox)
        return groupe

    def groupeMaree(self):
        """Initialisation des widgets du groupe Marée"""
        groupe = QGroupBox("Marée")
        self.lblMaree1 = QLabel("→")
        self.lblMaree2 = QLabel("→")
        vbox = QVBoxLayout()
        vbox.addWidget(self.lblMaree1)
        vbox.addWidget(self.lblMaree2)
        vbox.addStretch(0)
        groupe.setLayout(vbox)
        return groupe

    def groupeCap(self):
        """Initialisation des widgets du groupe Cap"""
        groupe = QGroupBox("Cap")
        lbl1 = QLabel("Cap compas:")
        self.capCompas = QLabel("→")
        lbl2 = QLabel("Route de fond:")
        self.routeFond = QLabel("→")
        lbl3 = QLabel("Route de surface")
        self.routeSurface = QLabel("→")
        vbox = QVBoxLayout()
        vbox.addWidget(lbl1)
        vbox.addWidget(self.capCompas)
        vbox.addWidget(lbl2)
        vbox.addWidget(self.routeFond)
        vbox.addWidget(lbl3)
        vbox.addWidget(self.routeSurface)
        vbox.addStretch(0)
        groupe.setLayout(vbox)
        return groupe

    def updateLabelsAmer(self, pos1, pos2):
        """
        mise à jour des labels du groupe position amer
        @type pos1: str
        @param pos1: position en deg, min, sec au nord
        @type pos2: str
        @param pos2: position en deg, min, sec a l'ouest
        """
        self.lblAmer1.setText(pos1)
        self.lblAmer2.setText(pos2)

    def updateLabelsGPS(self, pos1, pos2):
        """
        mise à jour des labels du groupe position GPS
        @type pos1: str
        @param pos1: position en deg, min, sec au nord
        @type pos2: str
        @param pos2: position en deg, min, sec a l'ouest
        """
        self.lblGPS1.setText(pos1)
        self.lblGPS2.setText(pos2)

    def updateLabelsError(self, pos1, pos2):
        """
        mise à jour des labels du groupe position GPS
        @type pos1: str
        @param pos1: position en deg, min, sec au nord
        @type pos2: str
        @param pos2: position en deg, min, sec a l'ouest
        """
        self.lblError1.setText(pos1)
        self.lblError2.setText(pos2)

    def updateMarre(self, lbl1=None, lbl2=None):
        """
        mise à jour des labels du groupe marée
        @type lbl1: str
        @param lbl1: contenu du lbl1
        @type lbl2: str
        @param lbl2: contenu du lbl2
        """
        if lbl1:
            self.lblMaree1.setText(lbl1)
        if lbl2:
            self.lblMaree2.setText(lbl2)

    def updateCap(self,  capCompas="", routeSurface="", routeFond="Non Implémenté"):
        """
        mise à jour des labels du groupe cap
        @param cap: contenu du lbl
        @type cap: str
        """
        self.capCompas.setText(capCompas)
        self.routeFond.setText(routeFond)
        self.routeSurface.setText(routeSurface)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    result = app.exec_()
    print("QT finished " + str(result))
    exit(result)
