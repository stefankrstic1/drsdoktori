from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt, QThread, QObject
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, time



class PlayerState(QObject):

    isJumping = False
    movingLeft = False
    movingRight = False
    jumpCount = 0
    dragance = QLabel
    positionX, positionY = 0, 0


    def __init__(self):
        super().__init__()
        self.thread = QThread()
        self.is_done = False

        self.moveToThread(self.thread)

        self.thread.started.connect(self.check)

    def start(self):
        self.thread.start()

    def check(self):
        #rec1 = dragan.geometry()
        while not self.is_done:
            if(self.isJumping == True):
                self.rec1 = self.dragance.geometry()
                while self.jumpCount < 40:
                    #ako se pomera i levo da pomeri i tamo
                    if(self.movingLeft == True):
                        self.dragance.setGeometry(self.rec1.x() - 5, self.rec1.y(), self.rec1.width(),
                                                  self.rec1.height())
                        self.rec1 = self.dragance.geometry()
                        self.movingLeft = False
                    #ako se pomera i desno da pomeri i tamo
                    if(self.movingRight == True):
                        self.dragance.setGeometry(self.rec1.x() + 5, self.rec1.y() , self.rec1.width(),
                                                  self.rec1.height())
                        self.rec1 = self.dragance.geometry()
                        self.movingRight = False
                    self.dragance.setGeometry(self.rec1.x(), self.rec1.y() - 5, self.rec1.width(), self.rec1.height())
                    self.jumpCount += 1
                    self.rec1 = self.dragance.geometry()
                    self.thread.msleep(1)
                self.isJumping = False
                self.jumpCount = 0
            time.sleep(0.001)

    def kill(self):
        self.is_done = True
        self.thread.quit()
