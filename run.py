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
        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QIcon("./icons/sailboat.png"))
        self.setWindowTitle(self.title)
        self.draw_toolbar()
        self.draw_map()
        self.show()

    def draw_toolbar(self):
        exitAct = QAction(self.style().standardIcon(QStyle.SP_DialogCloseButton), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

    def draw_map(self):
        self.setCentralWidget(DrawMap("./maps/baie_de_quiberon.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    result = app.exec_()
    print("QT finished " + str(result))
    exit(result)
