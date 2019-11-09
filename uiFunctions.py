#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QLabel, QGridLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QIntValidator


class GpsDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.map = parent
        self.setWindowTitle("Cordonnés GPS")
        lbl1 = QLabel("Entrez la position GPS")
        self.nDeg = QLineEdit()
        self.nDeg.setValidator(QIntValidator())
        self.nDeg.setText("47")
        self.nDeg.setMaxLength(2)
        deglbl = QLabel("°")
        self.nMin = QLineEdit()
        self.nMin.setValidator(QIntValidator())
        self.nMin.setText("25")
        self.nMin.setMaxLength(2)
        minlbl = QLabel("'")
        self.nSec = QLineEdit()
        self.nSec.setValidator(QDoubleValidator())
        self.nSec.setText("36,52")
        self.seclbl = QLabel('"')
        nlbl = QLabel("N")

        self.wDeg = QLineEdit()
        self.wDeg.setValidator(QIntValidator())
        self.wDeg.setMaxLength(2)
        self.wDeg.setText("2")
        deglbl2 = QLabel("°")
        self.wMin = QLineEdit()
        self.wMin.setValidator(QIntValidator())
        self.wMin.setMaxLength(2)
        self.wMin.setText("50")
        minlbl2 = QLabel("'")
        self.wSec = QLineEdit()
        self.wSec.setValidator(QDoubleValidator())
        self.wSec.setText("26,97")
        seclbl2 = QLabel('"')
        wlbl = QLabel("W")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QGridLayout()
        self.layout.addWidget(lbl1, 0, 0)
        self.layout.addWidget(self.nDeg, 1, 0)
        self.layout.addWidget(deglbl, 1, 1)
        self.layout.addWidget(self.nMin, 1, 2)
        self.layout.addWidget(minlbl, 1, 3)
        self.layout.addWidget(self.nSec, 1, 4)
        self.layout.addWidget(self.seclbl, 1, 5)
        self.layout.addWidget(nlbl, 1, 6)

        self.layout.addWidget(self.wDeg, 2, 0)
        self.layout.addWidget(deglbl2, 2, 1)
        self.layout.addWidget(self.wMin, 2, 2)
        self.layout.addWidget(minlbl2, 2, 3)
        self.layout.addWidget(self.wSec, 2, 4)
        self.layout.addWidget(seclbl2, 2, 5)
        self.layout.addWidget(wlbl, 2, 6)
        self.layout.addWidget(self.buttonBox, 3, 0)
        self.setLayout(self.layout)

    def ok(self):
        # try:
        ncoord = int(self.nDeg.text()), int(self.nMin.text()), float(self.nSec.text().replace(",", "."))
        wcoord = int(self.wDeg.text()), int(self.wMin.text()), float(self.wSec.text().replace(",", "."))
        self.map.getGpsCoordinates(ncoord, wcoord)
        self.accept()
    # except Exception:
    #    self.reject()
    #   QMessageBox.critical(self, "Cordonées invalides", "Les coordonnées sont invalides")
