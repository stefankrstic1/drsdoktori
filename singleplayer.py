from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random

from charachter import Charachter
from key_notifier import KeyNotifier


class SinglePlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = Charachter(self)
        self.initPrso()

    def initPrso(self):
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.label1.__update_position__)
        self.key_notifier.start()

        self.label1.setStyleSheet("background-image: url()")

        self.setStyleSheet("background-image: url(stageglavni.png)")




    def keyPressEvent(self, event):
        self.vx, self.vy = 0, 0
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())







