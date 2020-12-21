from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt, QThread, QObject
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, time

Platforms = [[820, 65, 1115], [640, 110, 250], [640, 525, 675], [640, 940, 1080],
             [455, 235, 945], [270, 105, 255], [270, 525, 675], [270, 940, 1080],
             [85, 250, 395], [85, 805, 949]]

class State(QObject):
    isJumping = False
    movingLeft = False
    movingRight = False
    isFalling = False
    onPlatform = False
    jumpCount = 0
    dragance = QLabel
    positionX, positionY = 0, 0

    def __init__(self):
        super().__init__()
        self.thread = QThread()
        self.is_done = False

        self.moveToThread(self.thread)

        self.thread.started.connect(self.check)
        #self.checkOnPlatform()

    def start(self):
        self.thread.start()

    def checkOnPlatform(self):
        self.rec1 = self.dragance.geometry()
        for x in Platforms:
            if(self.rec1.y() == x[0] and self.rec1.x() > x[1] and self.rec1.x() < x[2]):
                self.onPlatform = True
                break
            else:
                self.onPlatform = False


    def check(self):
        global Platforms
        #rec1 = dragan.geometry()
        while not self.is_done:
            #self.checkOnPlatform()
            if(self.isJumping == True):
                self.rec1 = self.dragance.geometry()
                while self.jumpCount < 40 :
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
                self.isFalling = True
                self.onPlatform = False
            elif((self.isFalling == True and self.onPlatform == False) or (self.isFalling == False and self.onPlatform == True)):
                self.checkOnPlatform()
                self.rec1 = self.dragance.geometry()
                while self.rec1.y() < 820 and self.onPlatform == False:
                    if (self.movingLeft == True):
                        self.dragance.setGeometry(self.rec1.x() - 5, self.rec1.y(), self.rec1.width(),
                                                  self.rec1.height())
                        self.rec1 = self.dragance.geometry()
                        self.movingLeft = False
                        # ako se pomera i desno da pomeri i tamo
                    if (self.movingRight == True):
                        self.dragance.setGeometry(self.rec1.x() + 5, self.rec1.y(), self.rec1.width(),
                                                  self.rec1.height())
                        self.rec1 = self.dragance.geometry()
                        self.movingRight = False
                    self.dragance.setGeometry(self.rec1.x(), self.rec1.y() + 5, self.rec1.width(), self.rec1.height())
                    self.rec1 = self.dragance.geometry()
                    self.thread.msleep(1)
                    self.checkOnPlatform()
                self.isFalling = False

            time.sleep(0.001)

    def kill(self):
        self.is_done = True
        self.thread.quit()
