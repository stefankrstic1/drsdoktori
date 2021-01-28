from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt, QThread ,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, time
import time, variables
from key_notifier import KeyNotifier
from playerstate import State




class Charachter(QLabel):

    def __init__(self, parent, broj):
        QLabel.__init__(self, parent)
        self.koji = broj
        self.initChar()
        self.jump = State(broj)
        self.jump.start()
        self.time = time.time()
        self.isJumping = False



    def initChar(self):
        if(self.koji == 0):
            self.pix1 = QPixmap('Slike/dragan.png')
            self.setPixmap(self.pix1.scaled(100, 100))
            self.setGeometry(202, 820, 100, 100)
            self.setFixedSize(100, 100)
            self.setStyleSheet("background-image: url()")
            variables.x = 200
            variables.y = 820
            timer = QTimer(self)
            timer.start(20)
            timer.timeout.connect(self.changePosition)
        elif(self.koji == 1):
            self.pix1 = QPixmap('Slike/goran.png')
            self.setPixmap(self.pix1.scaled(100, 100))
            self.setGeometry(1002, 820, 100, 100)
            self.setFixedSize(100, 100)
            self.setStyleSheet("background-image: url()")
            variables.x2 = 1002
            variables.y2 = 820
            timer = QTimer(self)
            timer.start(20)
            timer.timeout.connect(self.changePosition2)


    def changePosition(self):
        self.move(variables.x, variables.y)
        if variables.draganUbijen == True:
            self.setVisible(False)
        else:
            self.setVisible(True)
        if variables.levo == True:
            self.setPixmap(self.pix1.scaled(100, 100).transformed((QtGui.QTransform().scale(-1, 1))))
        else:
            self.setPixmap(self.pix1.scaled(100, 100))

    def changePosition2(self):
        self.move(variables.x2, variables.y2)
        if variables.draganUbijen2 == True:
            self.setVisible(False)
        else:
            self.setVisible(True)

        if variables.levo2 == True:
            self.setPixmap(self.pix1.scaled(100, 100).transformed((QtGui.QTransform().scale(-1, 1))))
        else:
            self.setPixmap(self.pix1.scaled(100, 100))

    def __update_position__(self, key):
        if self.koji == 0:
            if variables.draganUbijen == False:
                if key == Qt.Key_L:
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
        elif self.koji == 1:
            if variables.draganUbijen2 == False:
                if key == Qt.Key_X:
                    if self.bullet.shoot.ableToFire == True:
                        self.bullet.shoot.dragance = self
                        self.bullet.shoot.bullet = self.bullet
                        self.bullet.shoot.ableToFiare = False
                        self.bullet.shoot.fireing = True
                if key == Qt.Key_D:
                    self.jump.movingRight = True
                    self.bullet.shoot.okrenutLevo = False
                if key == Qt.Key_W:
                    self.jump.isJumping = True
                if key == Qt.Key_A:
                    self.jump.movingLeft = True
                    self.bullet.shoot.okrenutLevo = True
