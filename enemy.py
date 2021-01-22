from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush, QTransform
from PyQt5.QtCore import QSize, Qt, QThread ,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, time
import time, variables

class Enemy(QLabel):
    def __init__(self, parent, koordinate, broj):
        QLabel.__init__(self, parent)
        self.isHit = False
        self.init(koordinate[0], koordinate[1])
        self.koji = broj

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
        self.pozicija = self.geometry()
        if variables.Pokupio[self.koji] == True:
            self.setVisible(False)

        if variables.isShot == True:
            if (self.pozicija.x() < variables.bulletX and self.pozicija.x() + 100 > variables.bulletX) and (self.pozicija.y() - 50 < variables.bulletY  and self.pozicija.y() + 50 > variables.bulletY):
                self.isHit = True
                self.pix1 = QPixmap('Slike/krepo.png')
                self.setPixmap(self.pix1.scaled(100, 100))
                variables.aliveEnemy -= 1
                variables.deadEnemy += 1
                variables.Pogodjen[self.koji] = True
                variables.CurrentPosition[self.koji][0] = self.pozicija.x()
                variables.CurrentPosition[self.koji][1] = self.pozicija.y()

        if variables.Pogodjen[self.koji] == False:
            if (self.pozicija.x() - 50 < variables.x and self.pozicija.x() + 50 > variables.x) and (self.pozicija.y() - 50 < variables.y and self.pozicija.y() + 50 > variables.y):
                variables.draganUbijen = True

        if variables.draganUbijen == True:
            self.pix1 = QPixmap('Slike/enemy.png')
            self.setPixmap(self.pix1.scaled(100, 100))
            self.setVisible(True)

        if variables.x > variables.trenutnaPozicijaEnemy[self.koji][0] and variables.Pogodjen[self.koji] == False:
            variables.trenutnaPozicijaEnemy[self.koji][0] += 5
            if(variables.y > variables.trenutnaPozicijaEnemy[self.koji][1]):
                variables.trenutnaPozicijaEnemy[self.koji][1] += 4
            else:
                variables.trenutnaPozicijaEnemy[self.koji][1] -= 4
            self.setGeometry(variables.trenutnaPozicijaEnemy[self.koji][0], variables.trenutnaPozicijaEnemy[self.koji][1], 100, 100)
        elif variables.x < variables.trenutnaPozicijaEnemy[self.koji][0] and variables.Pogodjen[self.koji] == False:
            variables.trenutnaPozicijaEnemy[self.koji][0] -= 5
            if (variables.y > variables.trenutnaPozicijaEnemy[self.koji][1]):
                variables.trenutnaPozicijaEnemy[self.koji][1] += 4
            else:
                variables.trenutnaPozicijaEnemy[self.koji][1] -= 4
            self.setGeometry(variables.trenutnaPozicijaEnemy[self.koji][0], variables.trenutnaPozicijaEnemy[self.koji][1], 100, 100)