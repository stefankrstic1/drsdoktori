from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush, QTransform
from PyQt5.QtCore import QSize, Qt, QThread, QTimer
import sys
import random
import time
import variables

class Enemy(QLabel):
    def __init__(self, parent, koordinate, broj, dragance):
        QLabel.__init__(self, parent)
        self.dragan = dragance
        self.isHit = False
        variables.trenutnaPozicijaEnemy[broj] = koordinate
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

        if variables.gameLive == True:
            if((variables.CurrentPosition[self.koji][0] - 50 < variables.x and variables.CurrentPosition[self.koji][0] + 50 > variables.x) and
                    (variables.CurrentPosition[self.koji][1] - 50 < variables.y and variables.CurrentPosition[self.koji][1] + 50 > variables.y) and variables.Pokupio[self.koji]==False):
                variables.Pokupio[self.koji] = True
                variables.collectedEnemy += 1
                variables.points+=1
            if variables.Pogodjen[self.koji] == True:
                self.pix1 = QPixmap('Slike/krepo.png')
                self.setPixmap(self.pix1.scaled(100, 100))
            else:
                self.pix1 = QPixmap('Slike/enemy.png')
                self.setPixmap(self.pix1.scaled(100, 100))
                self.setVisible(True)

            self.pozicija = self.geometry()
            if variables.Pokupio[self.koji] == True:
                self.setVisible(False)

            if variables.isShot == True and variables.bulletused == False and variables.Pogodjen[self.koji] == False :
                if (self.pozicija.x() < variables.bulletX and self.pozicija.x() + 100 > variables.bulletX) and (self.pozicija.y() - 50 < variables.bulletY  and self.pozicija.y() + 50 > variables.bulletY):
                    self.isHit = True
                    variables.aliveEnemy -= 1
                    variables.deadEnemy += 1
                    variables.Pogodjen[self.koji] = True
                    variables.CurrentPosition[self.koji][0] = self.pozicija.x()
                    variables.CurrentPosition[self.koji][1] = self.pozicija.y()
                    variables.bulletused = True
                    variables.points += 1

            if variables.Pogodjen[self.koji] == False:
                if (self.pozicija.x() - 50 < variables.x and self.pozicija.x() + 50 > variables.x) and (self.pozicija.y() - 50 < variables.y and self.pozicija.y() + 50 > variables.y):
                    variables.draganUbijen = True
                    variables.takeLife = True

            if variables.Pogodjen[self.koji] == False and variables.draganUbijen == False:
                if variables.x > variables.trenutnaPozicijaEnemy[self.koji][0]:
                    variables.trenutnaPozicijaEnemy[self.koji][0] += 4 + variables.level / 2

                elif variables.x < variables.trenutnaPozicijaEnemy[self.koji][0]:
                    variables.trenutnaPozicijaEnemy[self.koji][0] -= 4 + variables.level / 2

                if variables.y > variables.trenutnaPozicijaEnemy[self.koji][1]:
                    variables.trenutnaPozicijaEnemy[self.koji][1] += 3 + variables.level / 2
                else:
                    variables.trenutnaPozicijaEnemy[self.koji][1] -= 3 + variables.level / 2

            if variables.draganUbijen == True:
                self.setVisible(True)
                variables.x = 200
                variables.y = 820
                variables.draganUbijen = False
                variables.Pogodjen = [False, False, False, False]
                variables.Pokupio = [False, False, False, False]
                variables.CurrentPosition = [[0, 0], [0, 0], [0, 0], [0, 0]]
                variables.trenutnaPozicijaEnemy = [random.randrange(100, 1000, 10), random.randrange(100, 500, 10)], \
                                                  [random.randrange(100, 1000, 10), random.randrange(100, 500, 10)], \
                                                  [random.randrange(100, 1000, 10), random.randrange(100, 500, 10)], \
                                                  [random.randrange(100, 1000, 10), random.randrange(100, 500, 10)]
                variables.aliveEnemy = 4
                variables.deadEnemy = 0
                variables.collectedEnemy = 0
                self.neSkaciKonju = True

            self.setGeometry(variables.trenutnaPozicijaEnemy[self.koji][0],
                             variables.trenutnaPozicijaEnemy[self.koji][1], 100, 100)

            if variables.collectedEnemy == 4:
                self.setVisible(True)
                variables.x = 200
                variables.y = 820
                variables.draganUbijen = False
                variables.Pogodjen = [False, False, False, False]
                variables.Pokupio = [False, False, False, False]
                variables.CurrentPosition = [[0, 0], [0, 0], [0, 0], [0, 0]]
                variables.trenutnaPozicijaEnemy = [random.randrange(100, 1000, 10), random.randrange(100, 500, 10)], \
                                                  [random.randrange(100, 1000, 10), random.randrange(100, 500, 10)], \
                                                  [random.randrange(100, 1000, 10), random.randrange(100, 500, 10)], \
                                                  [random.randrange(100, 1000, 10), random.randrange(100, 500, 10)]
                variables.aliveEnemy = 4
                variables.deadEnemy = 0
                variables.collectedEnemy = 0
                variables.increaseLevel = True
                self.neSkaciKonju = True
