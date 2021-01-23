from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random

from singleplayer import SinglePlayer

class UI(QtWidgets.QWidget):

    def init(self):

        self.StackedWidgets = QStackedWidget()
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        stack2 = SinglePlayer()
        self.MenuUI()

        self.MultiplayerUI()

        self.StackedWidgets.addWidget(self.stack1)
        self.StackedWidgets.addWidget(stack2)
        self.StackedWidgets.addWidget(self.stack3)

    def MenuUI(self):
        self.stack1.setFixedSize(1280, 960)

        layout = QVBoxLayout()

        oImage = QImage("Slike/pozadina.jpg")
        sImage = oImage.scaled(QSize(1280, 960))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.btn = QPushButton('SINGLEPLAYER',self.stack1)
        self.btn1 = QPushButton('MULTIPLAYER', self.stack1)
        self.btn2 = QPushButton('OPTIONS', self.stack1)
        self.btn3 = QPushButton('EXIT', self.stack1)



        #promeniti sliku za dugme!!!!!!!!!!!!
        self.btn.setStyleSheet("border-image: url(dugme1.png)")

        self.btn.setFixedSize(200, 80)
        self.btn1.setFixedSize(200, 80)
        self.btn2.setFixedSize(200, 80)
        self.btn3.setFixedSize(200, 80)
        layout.addWidget(self.btn)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.setAlignment(QtCore.Qt.AlignCenter)

        self.stack1.setLayout(layout)

    def MultiplayerUI(self):
        self.stack3.setStyleSheet("background: blue")

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2 - 50)


