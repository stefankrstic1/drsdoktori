from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random



class SinglePlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.initPrso()

    def initPrso(self):
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        self.setStyleSheet("background: red")



