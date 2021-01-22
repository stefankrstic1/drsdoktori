from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt, QThread ,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, time
import time, variables
from key_notifier import KeyNotifier
from playerstate import State




class Charachter(QLabel):

    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.initChar()
        self.jump = State()
        self.jump.start()
        self.time = time.time()
        self.isJumping = False

    def initChar(self):
        self.pix1 = QPixmap('Slike/dragan.png')
        self.setPixmap(self.pix1.scaled(100, 100))
        self.setGeometry(200, 820, 100, 100)
        self.setFixedSize(100, 100)
        self.setStyleSheet("background-image: url()")
        variables.x = 200
        variables.y = 820
        timer = QTimer(self)
        timer.start(20)
        timer.timeout.connect(self.changePosition)

    def changePosition(self):
        self.move(variables.x, variables.y)
        if variables.levo == True:
            self.setPixmap(self.pix1.scaled(100, 100).transformed((QtGui.QTransform().scale(-1, 1))))
        else:
            self.setPixmap(self.pix1.scaled(100, 100))

        if variables.draganUbijen == True:
            variables.x = 200
            variables.y = 820
            variables.draganUbijen = False
            variables.Pogodjen = [False, False, False, False]
            variables.Pokupio = [False, False, False, False]
            variables.CurrentPosition = [[0, 0], [0, 0], [0, 0], [0, 0]]
            variables.trenutnaPozicijaEnemy = [variables.pocetnaPozicijaPrvog, variables.pocetnaPozicijaDrugog, variables.pocetnaPozicijaTreceg, variables.pocetnaPozicijaCetvrtog]
            variables.aliveEnemy = 4
            variables.deadEnemy = 0
            variables.collectedEnemy = 0

    def __update_position__(self, key):
        if key == Qt.Key_Space:
            if self.bullet.shoot.ableToFire == True:
                self.bullet.shoot.dragance = self
                self.bullet.shoot.bullet = self.bullet
                self.bullet.shoot.ableToFire = False
                self.bullet.shoot.fireing = True
        if key == Qt.Key_Right:
            self.jump.movingRight = True
            self.bullet.shoot.okrenutLevo = False
        if key == Qt.Key_Up:
            self.jump.isJumping = True
        if key == Qt.Key_Left:
            self.jump.movingLeft = True
            self.bullet.shoot.okrenutLevo = True
