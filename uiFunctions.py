#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QLabel, QGridLayout, QLineEdit, QMessageBox, QGroupBox, \
    QVBoxLayout, QCheckBox
from PyQt5.QtGui import QDoubleValidator, QIntValidator


class GpsDialog(QDialog):
    """
    Interface de dialogue pour le GPS
    @author: Maxime Favier
    """

    def __init__(self, parent):
        """
        Initialisation des widgets
        @type parent: DrawMap
        @param parent: class parente DrawMap
        """
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
        """Fonction Valider"""
        try:
            ncoord = int(self.nDeg.text()), int(self.nMin.text()), float(self.nSec.text().replace(",", "."))
            wcoord = int(self.wDeg.text()), int(self.wMin.text()), float(self.wSec.text().replace(",", "."))
            self.map.getGpsCoordinates(ncoord, wcoord)
            self.accept()
        except Exception:
            self.reject()
            QMessageBox.critical(self, "Cordonées invalides", "Les coordonnées sont invalides")


class MareeDialog(QDialog):
    """Interface de dialogue pour le carculateur de marée
    @author: Maxime Favier
    """

    def __init__(self, parent, gparrent):
        """
        Initialisation des widgets
        @type parent: DrawMap
        @param parent: Classe parente DrawMap
        @type gparrent: Window
        @param gparrent: Classe de l'UI
        """
        super().__init__()
        self.map = parent
        self.ui = gparrent
        self.pmhauteur, self.pmheure, self.pmLendemain = None, None, None
        self.bmhauteur, self.bmheure, self.bmLendemain = None, None, None
        self.cHeure, self.cLendemain = None, None
        self.setWindowTitle("Marée Calculateur")

        lbl1 = QLabel("informations de marée")
        lbl2 = QLabel("Heure de calcul")
        self.cHeure = QLineEdit("")
        self.cHeure.setInputMask("d9:99")
        self.cLendemain = QCheckBox("+24h")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QGridLayout()
        self.layout.addWidget(lbl1, 0, 0)
        self.layout.addWidget(self.pleineMerGroupe(), 1, 0)
        self.layout.addWidget(self.basseMerGroupe(), 2, 0)
        self.layout.addWidget(lbl2, 3, 0)
        self.layout.addWidget(self.cHeure, 4, 0)
        self.layout.addWidget(self.cLendemain, 5, 0)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def pleineMerGroupe(self):
        """Initialisation des widgets pleine mer"""
        groupe = QGroupBox("Pleine mer")
        lbl1 = QLabel("Hauteur de l'eau")
        self.pmhauteur = QLineEdit()
        self.pmhauteur.setValidator(QDoubleValidator())
        lbl2 = QLabel("Heure de pleine mer")
        self.pmheure = QLineEdit("")
        self.pmheure.setInputMask("d9:99")
        self.pmLendemain = QCheckBox("+24h")
        vbox = QVBoxLayout()
        vbox.addWidget(lbl1)
        vbox.addWidget(self.pmhauteur)
        vbox.addWidget(lbl2)
        vbox.addWidget(self.pmheure)
        vbox.addWidget(self.pmLendemain)
        groupe.setLayout(vbox)
        return groupe

    def basseMerGroupe(self):
        """Initialisation des widgets basse mer"""
        groupe = QGroupBox("Basse mer")
        lbl1 = QLabel("Hauteur de l'eau")
        self.bmhauteur = QLineEdit()
        self.bmhauteur.setValidator(QDoubleValidator())
        lbl2 = QLabel("Heure de basse mer")
        self.bmheure = QLineEdit("")
        self.bmheure.setInputMask("d9:99")
        self.bmLendemain = QCheckBox("+24h")
        vbox = QVBoxLayout()
        vbox.addWidget(lbl1)
        vbox.addWidget(self.bmhauteur)
        vbox.addWidget(lbl2)
        vbox.addWidget(self.bmheure)
        vbox.addWidget(self.bmLendemain)
        groupe.setLayout(vbox)
        return groupe

    def ok(self):
        """Fonction valider"""
        pmHauteur = float(self.pmhauteur.text().replace(",", "."))
        bmHauteur = float(self.bmhauteur.text().replace(",", "."))
        heure, min = self.pmheure.text().split(":")
        pmheure = int(heure) * 60 + int(min) + 1440 if self.pmLendemain.isChecked() else int(heure) * 60 + int(min)
        # print(pmheure)
        heure, min = self.bmheure.text().split(":")
        bmheure = int(heure) * 60 + int(min) + 1440 if self.bmLendemain.isChecked() else int(heure) * 60 + int(min)
        # print(bmheure)
        heure, min = self.cHeure.text().split(":")
        cHeure = int(heure) * 60 + int(min) + 1440 if self.cLendemain.isChecked() else int(heure) * 60 + int(min)
        # print(cheure)
        self.ui.updateMarre("A {}:{}".format(heure, min), None)
        self.map.mareeProcessing(pmheure, pmHauteur, bmheure, bmHauteur, cHeure)
        self.accept()


class PositionTheorique(QDialog):
    """Interface graphique pour le calcul de la position theorique
    @author: Maxime Favuer"""

    def __init__(self, parent, gparent):
        """
        Initialisation des widgets
        @type parent: DrawMap
        @param parent: Classe parente DrawMap
        @type gparrent: Window
        @param gparrent: Classe de l'UI
        """
        super().__init__()
        self.map = parent
        self.ui = gparent
        self.courantAngle, self.deriveVent, self.declinaison, self.capCompas, self.deviation = None, None, None, None, None
        self.setWindowTitle("Calcul de la position théorique")

        lbl1 = QLabel("Calcul de la position théorique apres x minutes")

        lbl2 = QLabel("Entrez la position GPS")
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
        self.layout.addWidget(self.courantGroupe(), 1, 0, 1, 7)
        self.layout.addWidget(self.capGroupe(), 2, 0, 1, 7)
        # self.layout.addWidget(self.deriveVentGroupe(), 3, 0, 1, 7)

        self.layout.addWidget(lbl2, 4, 0, )
        self.layout.addWidget(self.nDeg, 5, 0)
        self.layout.addWidget(deglbl, 5, 1)
        self.layout.addWidget(self.nMin, 5, 2)
        self.layout.addWidget(minlbl, 5, 3)
        self.layout.addWidget(self.nSec, 5, 4)
        self.layout.addWidget(self.seclbl, 5, 5)
        self.layout.addWidget(nlbl, 5, 6)

        self.layout.addWidget(self.wDeg, 6, 0)
        self.layout.addWidget(deglbl2, 6, 1)
        self.layout.addWidget(self.wMin, 6, 2)
        self.layout.addWidget(minlbl2, 6, 3)
        self.layout.addWidget(self.wSec, 6, 4)
        self.layout.addWidget(seclbl2, 6, 5)
        self.layout.addWidget(wlbl, 6, 6)
        self.layout.addWidget(self.TempsGroupe(), 7, 0, 1, 7)
        self.layout.addWidget(self.buttonBox, 8, 0, 1, 7)
        self.setLayout(self.layout)

    def courantGroupe(self):
        # courrant deg + m/s
        groupe = QGroupBox("Information de courant")
        lbl1 = QLabel("Angle du courant")
        self.courantAngle = QLineEdit()
        self.courantAngle.setValidator(QDoubleValidator())
        lbl2 = QLabel("Vitesse du courant m/s")
        self.courantVitesse = QLineEdit()
        self.courantVitesse.setValidator(QDoubleValidator())
        vbox = QVBoxLayout()
        vbox.addWidget(lbl1)
        vbox.addWidget(self.courantAngle)
        vbox.addWidget(lbl2)
        vbox.addWidget(self.courantVitesse)
        groupe.setLayout(vbox)
        return groupe

    def capGroupe(self):
        # cap degre
        groupe = QGroupBox("Information Cap")
        lbl1 = QLabel("Cap compas")
        self.capCompas = QLineEdit()
        self.capCompas.setValidator(QDoubleValidator())
        lbl2 = QLabel("Déclinaison")
        self.declinaison = QLineEdit()
        self.declinaison.setValidator(QDoubleValidator())
        lbl3 = QLabel("déviation")
        self.deviation = QLineEdit()
        self.deviation.setValidator(QDoubleValidator())
        lbl4 = QLabel("Dérive du vent (°)")
        self.deriveVent = QLineEdit()
        self.deriveVent.setValidator(QDoubleValidator(0.00, 360, 2))
        vbox = QVBoxLayout()
        vbox.addWidget(lbl1)
        vbox.addWidget(self.capCompas)
        vbox.addWidget(lbl2)
        vbox.addWidget(self.declinaison)
        vbox.addWidget(lbl3)
        vbox.addWidget(self.deviation)
        vbox.addWidget(lbl4)
        vbox.addWidget(self.deriveVent)
        groupe.setLayout(vbox)
        return groupe

    def TempsGroupe(self):
        # temps en minutes pour la simulation
        groupe = QGroupBox("Information temps de simulation")
        lbl1 = QLabel("X minutes (min)")
        self.xMin = QLineEdit()
        self.xMin.setValidator(QIntValidator())
        vbox = QVBoxLayout()
        vbox.addWidget(lbl1)
        vbox.addWidget(self.xMin)
        groupe.setLayout(vbox)
        return groupe

    def ok(self):
        ncoord = int(self.nDeg.text()), int(self.nMin.text()), float(self.nSec.text().replace(",", "."))
        wcoord = int(self.wDeg.text()), int(self.wMin.text()), float(self.wSec.text().replace(",", "."))
        angleCourant = float(self.courantAngle.text())
        vitesseCourant = float(self.courantVitesse.text())
        capCompas = float(self.capCompas.text())
        declinaison = float(self.declinaison.text())
        deviation = float(self.deviation.text())
        deriveVent = float(self.deriveVent.text())
        xMin = int(self.xMin.text())
        # print(angleCourant, vitesseCourant, capCompas, declinaison, deviation, deriveVent, xMin)
        # print(ncoord, wcoord)
        self.map.posTheoriqueProcessing(ncoord, wcoord, angleCourant, vitesseCourant, capCompas, declinaison, deviation,
                                        deriveVent, xMin)
        self.accept()
