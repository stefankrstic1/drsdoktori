from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt, QThread ,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, time
import time, variables

class Enemy(QLabel):
    def __init__(self, parent, koordinate):
        QLabel.__init__(self, parent)
        self.isHit = False
        self.init(koordinate[0], koordinate[1])

    def init(self, x, y):
        self.pix1 = QPixmap('Slike/enemy.png')
        self.setPixmap(self.pix1.scaled(100, 100))
        self.setGeometry(x, y, 100, 100)
        self.setFixedSize(100, 100)
        self.setStyleSheet("background-image: url()")
        timer = QTimer(self)
        timer.start(20)
        timer.timeout.connect(self.changePosition)

    def changePosition(self):
        if variables.isShot == True:
            self.pozicija = self.geometry()
            if (self.pozicija.x() < variables.bulletX and self.pozicija.x() + 100 > variables.bulletX) and (self.pozicija.y() - 50 < variables.bulletY  and self.pozicija.y() + 50 > variables.bulletY):
                self.isHit = True
                self.pix1 = QPixmap('Slike/krepo.png')
                self.setPixmap(self.pix1.scaled(100,100))
        '''if variables.Levo == True:
            self.setPixmap(self.pix1.scaled(100, 100).transformed((QtGui.QTransform().scale(-1, 1))))
        else:
            self.setPixmap(self.pix1.scaled(100, 100))'''