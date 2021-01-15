from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, variables

from charachter import Charachter
from key_notifier import KeyNotifier
from bullet import Bullet
from enemy import Enemy
global label1
global label2

class SinglePlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = Charachter(self)
        self.label2 = Bullet(self)
        self.enemyLabel1 = Enemy(self, variables.pozicijaPrvog)
        self.enemyLabel2 = Enemy(self, variables.pozicijaDrugog)
        self.enemyLabel3 = Enemy(self, variables.pozicijaTreceg)
        self.enemyLabel4 = Enemy(self, variables.pozicijaCetvrtog)
        self.initPrso()
        self.label2.dragance = self.label1
        self.label1.bullet = self.label2

    def initPrso(self):
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.label1.__update_position__)
       # self.key_notifier.key_signal.connect(self.label2.__update_position__z)
        self.key_notifier.start()

        self.label1.setStyleSheet("background-image: url()")

        self.setStyleSheet("background-image: url(Slike/stageglavni.png)")

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())







