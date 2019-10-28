#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAction, qApp, QMainWindow,QStyle
from PyQt5.QtGui import QIcon, QStyleHints

from map import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Boat buddy"
        self.centralWidg = DrawMap("./maps/baie_de_quiberon.png")
        self.init_ui()

    def init_ui(self):
        """definitions des proprietés du GUI"""
        self.setWindowIcon(QIcon("./icons/sailboat.png"))
        self.setWindowTitle(self.title)
        self.draw_toolbar()
        self.draw_map()
        self.show()

    def draw_toolbar(self):
        """Creation des bouttons de la barre de tache"""
        exitAct = QAction(self.style().standardIcon(QStyle.SP_DialogCloseButton), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        positionTool = QAction(QIcon("./icons/star.png"), "Position Tool", self)
        positionTool.setToolTip('Calcule la position')
        delPositionTool = QAction(QIcon("./icons/delStar.png"), "Position Tool", self)
        delPositionTool.setToolTip('Supprime le tracé des amer')
        delPositionTool.triggered.connect(self.centralWidg.supprimerTraces)

        mareeTool = QAction(QIcon("./icons/maree.png"), "Maree Option", self)
        mareeTool.setToolTip("Calcul de la marée")

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(positionTool)
        self.toolbar.addAction(delPositionTool)
        self.toolbar.addAction(mareeTool)
        self.toolbar.addAction(exitAct)

    def draw_map(self):
        """positionement de la carte"""
        self.setCentralWidget(self.centralWidg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    result = app.exec_()
    print("QT finished " + str(result))
    exit(result)
