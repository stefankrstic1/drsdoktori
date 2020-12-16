from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random

from key_notifier import KeyNotifier


class Charachter(QLabel):

    def __init__(self, parent):
        QLabel.__init__(self, parent)

        self.initChar()

        self.vx, self.vy = 0, 0


    def initChar(self):

        self.pix1 = QPixmap('dragan.png')
        self.setPixmap(self.pix1.scaled(100, 100))
        self.setGeometry(200,820, 100, 100)
        self.setFixedSize(100, 100)


    def keyPressEvent(self, event):
        self.vx, self.vy = 0, 0
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):
        rec1 = self.geometry()

        if key == Qt.Key_Right:
            self.setGeometry(rec1.x() + 5, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            self.setGeometry(rec1.x(), rec1.y() + 5, rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            self.setGeometry(rec1.x(), rec1.y() - 5, rec1.width(), rec1.height())

        elif key == Qt.Key_Left:
            self.setGeometry(rec1.x() - 5, rec1.y(), rec1.width(), rec1.height())

    def closeEvent(self, event):
        self.key_notifier.die()