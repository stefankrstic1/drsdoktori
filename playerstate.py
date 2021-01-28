from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, QObject
from PyQt5 import QtGui, QtWidgets
import time

import variables

Platforms = [[820, 0, 1280], [640, 110, 250], [640, 525, 675], [640, 940, 1080],
             [455, 235, 945], [270, 105, 255], [270, 525, 675], [270, 940, 1080],
             [85, 250, 395], [85, 805, 949]]

movingLeft = False
movingRight = False

class State(QObject):
    isJumping = False
    movingLeft = False
    movingRight = False
    isFalling = False
    onPlatform = True
    jumpCount = 0

    def __init__(self, broj):
        super().__init__()
        self.thread = QThread()
        self.koji = broj
        self.is_done = False
        self.moveToThread(self.thread)
        if self.koji == 0:
            self.pix1 = QPixmap('Slike/dragan.png')
        else:
            self.pix1 = QPixmap('Slike/goran.png')
        self.thread.started.connect(self.check)
        self.neSkaciKonju = False
        #self.checkOnPlatform()

    def start(self):
        self.thread.start()

    def checkOnPlatform(self):
        self.rec1 = [variables.x, variables.y]
        for x in Platforms:
            if(self.rec1[1] < x[0] + 30 and self.rec1[1] > x[0] and self.rec1[0] > x[1] and self.rec1[0] < x[2]):
                self.onPlatform = True
                self.isFalling = False
                break
            else:
                self.onPlatform = False
                self.isFalling = True

    def checkOnPlatform2(self):
        self.rec1 = [variables.x2, variables.y2]
        for x in Platforms:
            if(self.rec1[1] < x[0] + 30 and self.rec1[1] > x[0] and self.rec1[0] > x[1] and self.rec1[0] < x[2]):
                self.onPlatform = True
                self.isFalling = False
                break
            else:
                self.onPlatform = False
                self.isFalling = True


    def check(self):
        if self.koji == 0:
            while not self.is_done:
                if(self.isJumping == True and self.onPlatform == True):
                    while self.jumpCount < 40 and variables.y > 20:
                        #ako se pomera i levo da pomeri i tamo
                        if(self.movingLeft == True and variables.x > 65):
                            variables.levo = True
                            variables.x -= 5 + variables.level / 2
                            self.movingLeft = False
                        #ako se pomera i desno da pomeri i tamo
                        if(self.movingRight == True and variables.x < 1115):
                            variables.levo = False
                            variables.x += 5 + variables.level / 2
                            self.movingRight = False
                        if (self.neSkaciKonju == True):
                            self.onPlatform = True
                            self.isJumping = False
                            self.isFalling = False
                            break
                        variables.y -= 5
                        self.jumpCount += 1
                        self.thread.msleep(1)
                    self.isJumping = False
                    self.jumpCount = 0
                    self.isFalling = True
                    self.onPlatform = False
                elif(self.isFalling == True):
                    while self.onPlatform == False:
                        if (self.movingLeft == True and variables.x > 65):
                            variables.levo = True
                            variables.x -= 5 + variables.level / 2
                            self.movingLeft = False
                            # ako se pomera i desno da pomeri i tamo
                        if (self.movingRight == True and variables.x < 1115):
                            variables.levo = False
                            variables.x += 5 + variables.level / 2
                            self.movingRight = False
                        if(self.neSkaciKonju == True):
                            self.onPlatform = True
                            self.isJumping = False
                            self.isFalling = False
                            break
                        variables.y += 5
                        self.thread.msleep(1)
                        self.checkOnPlatform()
                    self.isFalling = False
                elif (self.onPlatform == True and self.movingRight == True and variables.x < 1115):
                    variables.levo = False
                    variables.x += 5 + variables.level / 2
                    self.checkOnPlatform()
                    self.movingRight = False

                elif (self.onPlatform == True and self.movingLeft == True and variables.x > 65):
                    variables.levo = True
                    variables.x -= 5 + variables.level / 2
                    self.checkOnPlatform()
                    self.movingLeft = False
                #self.dragance.update()
                time.sleep(0.01)
        elif self.koji == 1:
            while not self.is_done:
                if (self.isJumping == True and self.onPlatform == True):
                    while self.jumpCount < 40 and variables.y2 > 20:
                        # ako se pomera i levo da pomeri i tamo
                        if (self.movingLeft == True and variables.x2 > 65):
                            variables.levo2 = True
                            variables.x2 -= 5 + variables.level / 2
                            self.movingLeft = False
                        # ako se pomera i desno da pomeri i tamo
                        if (self.movingRight == True and variables.x2 < 1115):
                            variables.levo2 = False
                            variables.x2 += 5 + variables.level / 2
                            self.movingRight = False
                        if (self.neSkaciKonju == True):
                            self.onPlatform = True
                            self.isJumping = False
                            self.isFalling = False
                            break
                        variables.y2 -= 5
                        self.jumpCount += 1
                        self.thread.msleep(1)
                    self.isJumping = False
                    self.jumpCount = 0
                    self.isFalling = True
                    self.onPlatform = False
                elif (self.isFalling == True):
                    while self.onPlatform == False:
                        if (self.movingLeft == True and variables.x2 > 65):
                            variables.levo = True
                            variables.x2 -= 5 + variables.level / 2
                            self.movingLeft = False
                            # ako se pomera i desno da pomeri i tamo
                        if (self.movingRight == True and variables.x2 < 1115):
                            variables.levo = False
                            variables.x2 += 5 + variables.level / 2
                            self.movingRight = False
                        if (self.neSkaciKonju == True):
                            self.onPlatform = True
                            self.isJumping = False
                            self.isFalling = False
                            break
                        variables.y2 += 5
                        self.thread.msleep(1)
                        self.checkOnPlatform2()
                    self.isFalling = False
                elif (self.onPlatform == True and self.movingRight == True and variables.x2 < 1115):
                    variables.levo2 = False
                    variables.x2 += 5 + variables.level / 2
                    self.checkOnPlatform2()
                    self.movingRight = False

                elif (self.onPlatform == True and self.movingLeft == True and variables.x2 > 65):
                    variables.levo2 = True
                    variables.x2 -= 5 + variables.level / 2
                    self.checkOnPlatform2()
                    self.movingLeft = False
                # self.dragance.update()
                time.sleep(0.01)

    def kill(self):
        self.is_done = True
        self.thread.quit()
