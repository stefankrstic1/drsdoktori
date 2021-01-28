from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush, QTransform
from PyQt5.QtCore import QSize, Qt, QThread, QTimer
import sys
import random
import time
import variables
import math


class Enemy(QLabel):
    def __init__(self, parent, koordinate, broj, dragance, nekiBroj):
        QLabel.__init__(self, parent)
        self.dragan = dragance
        self.kojiBroj = nekiBroj
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
        if variables.gameLive == True and self.kojiBroj == 0:
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

            self.whereToGo2()

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

        elif variables.gameMultiLive == True and self.kojiBroj == 1:
            if variables.lives == 0 and variables.lives2 == 0:
                variables.gameOver = True

            if ((variables.CurrentPosition[self.koji][0] - 50 < variables.x and
                 variables.CurrentPosition[self.koji][0] + 50 > variables.x) and
                    (variables.CurrentPosition[self.koji][1] - 50 < variables.y and
                     variables.CurrentPosition[self.koji][1] + 50 > variables.y) and
                    variables.Pokupio[self.koji] == False):
                variables.Pokupio[self.koji] = True
                variables.collectedEnemy += 1
                variables.points += 1

            #DRUGI LIK
            if ((variables.CurrentPosition[self.koji][0] - 50 < variables.x2 and
                 variables.CurrentPosition[self.koji][0] + 50 > variables.x2) and
                    (variables.CurrentPosition[self.koji][1] - 50 < variables.y2 and
                     variables.CurrentPosition[self.koji][1] + 50 > variables.y2) and
                    variables.Pokupio[self.koji] == False):
                variables.Pokupio[self.koji] = True
                variables.collectedEnemy += 1
                variables.points2 += 1

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
            #PRVI LIK
            if variables.isShot == True and variables.bulletused == False and variables.Pogodjen[self.koji] == False:
                if (self.pozicija.x() < variables.bulletX and self.pozicija.x() + 100 > variables.bulletX) and (
                        self.pozicija.y() - 50 < variables.bulletY and self.pozicija.y() + 50 > variables.bulletY):
                    self.isHit = True
                    variables.aliveEnemy -= 1
                    variables.deadEnemy += 1
                    variables.Pogodjen[self.koji] = True
                    variables.CurrentPosition[self.koji][0] = self.pozicija.x()
                    variables.CurrentPosition[self.koji][1] = self.pozicija.y()
                    variables.bulletused = True
                    variables.points += 1
            #DRUGI LIK
            elif variables.isShot2 == True and variables.bulletused2 == False and variables.Pogodjen[self.koji] == False:
                if (self.pozicija.x() < variables.bullet2X and self.pozicija.x() + 100 > variables.bullet2X) and (self.pozicija.y() - 50 < variables.bullet2Y and self.pozicija.y() + 50 > variables.bullet2Y):
                    self.isHit = True
                    variables.aliveEnemy -= 1
                    variables.deadEnemy += 1
                    variables.Pogodjen[self.koji] = True
                    variables.CurrentPosition[self.koji][0] = self.pozicija.x()
                    variables.CurrentPosition[self.koji][1] = self.pozicija.y()
                    variables.bulletused2 = True
                    variables.points2 += 1

            if variables.Pogodjen[self.koji] == False:
                if (self.pozicija.x() - 50 < variables.x and self.pozicija.x() + 50 > variables.x) and (
                        self.pozicija.y() - 50 < variables.y and self.pozicija.y() + 50 > variables.y) and variables.draganUbijen == False:
                    variables.draganUbijen = True
                    variables.takeLife = True

            if variables.Pogodjen[self.koji] == False:
                if (self.pozicija.x() - 50 < variables.x2 and self.pozicija.x() + 50 > variables.x2) and (
                        self.pozicija.y() - 50 < variables.y2 and self.pozicija.y() + 50 > variables.y2) and variables.draganUbijen2 == False:
                    variables.draganUbijen2 = True
                    variables.takeLife2 = True

            self.whereToGo()

            if variables.draganUbijen == True and variables.draganUbijen2 == True:
                self.setVisible(True)
                variables.x = 200
                variables.y = 820
                variables.x2 = 1002
                variables.y2 = 820
                if variables.lives != 0:
                    variables.draganUbijen = False
                if variables.lives2 != 0:
                    variables.draganUbijen2 = False
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
                variables.x2 = 1002
                variables.y2 = 820
                if variables.lives != 0:
                    variables.draganUbijen = False
                if variables.lives2 != 0:
                    variables.draganUbijen2 = False
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

    def whereToGo2(self):
        if variables.Pogodjen[self.koji] == False:
            if (variables.x - 5 < variables.trenutnaPozicijaEnemy[self.koji][0] and variables.x + 5 >variables.trenutnaPozicijaEnemy[self.koji][0]):
                variables.trenutnaPozicijaEnemy[self.koji][0] = variables.x
            else:
                if(variables.x > variables.trenutnaPozicijaEnemy[self.koji][0]):
                    self.setPixmap(self.pix1.scaled(100, 100).transformed((QTransform().scale(-1, 1))))
                    variables.trenutnaPozicijaEnemy[self.koji][0] += 4 + variables.level / 2
                else:
                    self.setPixmap(self.pix1.scaled(100, 100))
                    variables.trenutnaPozicijaEnemy[self.koji][0] -= 4 + variables.level / 2
            if (variables.y - 5 < variables.trenutnaPozicijaEnemy[self.koji][1] and variables.y + 5 >
                    variables.trenutnaPozicijaEnemy[self.koji][1]):
                variables.trenutnaPozicijaEnemy[self.koji][1] = variables.y
            else:
                if (variables.y > variables.trenutnaPozicijaEnemy[self.koji][1]):
                    variables.trenutnaPozicijaEnemy[self.koji][1] += 3 + variables.level / 2
                else:
                    variables.trenutnaPozicijaEnemy[self.koji][1] -= 3 + variables.level / 2

    def whereToGo(self):
        if variables.Pogodjen[self.koji] == False:
            dalekoOdDraganX = abs(variables.x - variables.trenutnaPozicijaEnemy[self.koji][0])
            dalekoOdGoranX = abs(variables.x2 - variables.trenutnaPozicijaEnemy[self.koji][0])
            dalekoOdDraganY = abs(variables.y - variables.trenutnaPozicijaEnemy[self.koji][1])
            dalekoOdGoranY = abs(variables.y2 - variables.trenutnaPozicijaEnemy[self.koji][1])

            c1 = math.sqrt(math.pow(dalekoOdDraganX, 2) + math.pow(dalekoOdDraganY, 2))
            c2 = math.sqrt(math.pow(dalekoOdGoranX, 2) + math.pow(dalekoOdGoranY, 2))


            if (c1 > c2 and variables.draganUbijen2 == False) or variables.draganUbijen == True:
                if(variables.x2 - 5 < variables.trenutnaPozicijaEnemy[self.koji][0] and variables.x2 + 5 > variables.trenutnaPozicijaEnemy[self.koji][0]):
                    variables.trenutnaPozicijaEnemy[self.koji][0] = variables.x2
                else:
                    if(variables.x2 > variables.trenutnaPozicijaEnemy[self.koji][0]):
                        self.setPixmap(self.pix1.scaled(100, 100).transformed((QTransform().scale(-1, 1))))
                        variables.trenutnaPozicijaEnemy[self.koji][0] += 4 + variables.level / 2
                    else:
                        self.setPixmap(self.pix1.scaled(100, 100))
                        variables.trenutnaPozicijaEnemy[self.koji][0] -= 4 + variables.level / 2
                if(variables.y2 - 5 < variables.trenutnaPozicijaEnemy[self.koji][1] and variables.y2 + 5 > variables.trenutnaPozicijaEnemy[self.koji][1]):
                    variables.trenutnaPozicijaEnemy[self.koji][1] = variables.y2
                else:
                    if (variables.y2 > variables.trenutnaPozicijaEnemy[self.koji][1]):
                        variables.trenutnaPozicijaEnemy[self.koji][1] += 3 + variables.level / 2
                    else:
                        variables.trenutnaPozicijaEnemy[self.koji][1] -= 3 + variables.level / 2
            else:
                if (variables.x - 5 < variables.trenutnaPozicijaEnemy[self.koji][0] and variables.x + 5 >variables.trenutnaPozicijaEnemy[self.koji][0]):
                    variables.trenutnaPozicijaEnemy[self.koji][0] = variables.x
                else:
                    if(variables.x > variables.trenutnaPozicijaEnemy[self.koji][0]):
                        self.setPixmap(self.pix1.scaled(100, 100).transformed((QTransform().scale(-1, 1))))
                        variables.trenutnaPozicijaEnemy[self.koji][0] += 4 + variables.level / 2
                    else:
                        self.setPixmap(self.pix1.scaled(100, 100))
                        variables.trenutnaPozicijaEnemy[self.koji][0] -= 4 + variables.level / 2
                if (variables.y - 5 < variables.trenutnaPozicijaEnemy[self.koji][1] and variables.y + 5 >
                        variables.trenutnaPozicijaEnemy[self.koji][1]):
                    variables.trenutnaPozicijaEnemy[self.koji][1] = variables.y
                else:
                    if (variables.y > variables.trenutnaPozicijaEnemy[self.koji][1]):
                        variables.trenutnaPozicijaEnemy[self.koji][1] += 3 + variables.level / 2
                    else:
                        variables.trenutnaPozicijaEnemy[self.koji][1] -= 3 + variables.level / 2


