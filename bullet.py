from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush, QPainterPath
from PyQt5.QtCore import QSize, Qt, QThread
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, time
from key_notifier import KeyNotifier
from playerstate import State
from charachter import Charachter


class Bullet(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.resize(115,60)
        self.initBullet()


    def initBullet(self):
        character  = Charachter(self)
        rec1 = character.geometry()
        self.pix2 = QPixmap('bullet.png')
        self.setPixmap(self.pix2.scaled(30, 30))
        self.setStyleSheet("background-image: url()")
        self.setGeometry(rec1.x() + 100 , rec1.y() + 20 , 30, 30)
        self.setFixedSize(30, 30)

    def __update_position__(self, key):
        position = self.geometry()
        if key == Qt.Key_Space:
             self.setGeometry(position.x() + 2, position.y(), position.width(), position.height())
             position = self.geometry()

