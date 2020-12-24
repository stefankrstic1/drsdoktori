from PyQt5.QtWidgets import *

from PyQt5.QtCore import QThread, QObject

import time, gc

class BulletState(QGraphicsObject):
    dragance = QLabel
    bullet = QLabel
    fireing = False
    ableToFire = True
    okrenutLevo = False
    oduzimaj = False
    p = 0

    def __init__(self):
        super().__init__()
        self.thread = QThread()
        self.is_done = False

        self.moveToThread(self.thread)


        self.thread.started.connect(self.fire)

    def start(self):
        self.thread.start()

    def fire(self):
        while not self.is_done:
            if self.fireing == True:
                self.fireing = False
                self.bullet.setVisible(True)
                self.position = self.dragance.geometry()
                self.x = self.position.x()
                self.oduzimaj = True
                if self.okrenutLevo == False:
                    self.x += 70
                    self.oduzimaj = False
                while self.p < 50:
                    if(self.oduzimaj == False):
                        self.bullet.setGeometry(self.x, self.position.y() + 30, 30, 30)
                        self.x += 10
                        self.p += 1
                        self.thread.msleep(1)
                    else:
                        self.bullet.setGeometry(self.x, self.position.y() + 30, 30, 30)
                        self.x -= 10
                        self.p += 1
                        self.thread.msleep(1)
                self.fireing = False
                self.ableToFire = True
                self.p = 0
                self.bullet.setVisible(False)
            time.sleep(0.001)
