from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt, QThread
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, time

from key_notifier import KeyNotifier
from playerstate import State




class Charachter(QLabel):

    def __init__(self, parent):
        QLabel.__init__(self, parent)

        self.initChar()
        self.jump = State()
        self.jump.start()
        self.time = time.time()

        self.vx, self.vy = 0, 0
        self.isJumping = False


    def initChar(self):
        self.pix1 = QPixmap('dragan.png')
        self.setPixmap(self.pix1.scaled(100, 100))
        self.setGeometry(200, 820, 100, 100)
        self.setFixedSize(100, 100)

        self.jumpCount = 0

    def __update_position__(self, key):
        rec1 = self.geometry()

        if key == Qt.Key_Right:
            if(rec1.x() < 1115 and self.jump.isJumping == False and self.jump.isFalling == False):
                self.setPixmap(self.pix1.scaled(100, 100))
                self.setGeometry(rec1.x() + 5, rec1.y(), rec1.width(), rec1.height())
            elif(rec1.x() < 1115 and (self.jump.isJumping == True or self.jump.isFalling == True)):
                self.setPixmap(self.pix1.scaled(100, 100))
                self.jump.movingRight = True

        if key == Qt.Key_Up:
            #promenuti if da bude provera da li je na platformi a ne vreme
<<<<<<< HEAD
            if(self.jump.isJumping == False and self.jump.isFalling == False):
=======
            if(rec1.y() > 200 and time.time() - self.time  > 1):
>>>>>>> ab4417225b2b3450a59e84fa55b98731770b357c
                self.jump.isJumping = True
                self.jump.dragance = self


        if key == Qt.Key_Left:
            if (rec1.x() > 65 and self.jump.isJumping == False and self.jump.isFalling == False):
                self.setPixmap(self.pix1.scaled(100, 100).transformed((QtGui.QTransform().scale(-1, 1))))
                self.setGeometry(rec1.x() - 5, rec1.y(), rec1.width(), rec1.height())
            elif(rec1.x() > 65 and (self.jump.isJumping == True or self.jump.isFalling == True)):
                self.setPixmap(self.pix1.scaled(100, 100).transformed((QtGui.QTransform().scale(-1, 1))))
                self.jump.movingLeft = True
#komentar

    def closeEvent(self, event):
        self.key_notifier.die()

