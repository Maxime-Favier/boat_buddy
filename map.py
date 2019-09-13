from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QLabel, QGroupBox, QGridLayout, QVBoxLayout, \
    QSizePolicy
from PyQt5.QtGui import QIcon, QPainter, QBrush, QColor, QPen, QPixmap
from PIL import Image

class DrawMap(QWidget):
    def __init__(self, im):
        super().__init__()
        self.im = im
        image = Image.open(im)
        self.setMinimumWidth(image.size[0])
        self.setMinimumHeight(image.size[1])
        self.init_ui()

    def init_ui(self):
        pixmap = QPixmap(self.im)
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
