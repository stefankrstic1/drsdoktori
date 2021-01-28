from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, threading, variables, time

class ReturnScreen(QWidget):

    def __init__(self, sw):
        super().__init__()
        self.sw = sw
        self.init()

    def init(self):
        self.setFixedSize(1280, 960)

        layout = QVBoxLayout()

        self.setStyleSheet("background-image: url(Slike/gameOverScreen.jpg)")

        self.btn = QPushButton(self)

        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.btn.clicked.connect(self.returnToMenu)
        self.btn.setFixedSize(1280, 960)

        self.setLayout(layout)

        thread = threading.Thread(target=self.krajIgre)
        thread.start()

    def krajIgre(self):
        while True:
            if variables.gameOver == True:
                self.sw.setCurrentIndex(3)
                variables.gameOver = False
                variables.gameLive = False
                variables.gameMultiLive = False
                variables.draganUbijen2 = False
                variables.draganUbijen = False
                variables.reset = True
            time.sleep(0.3)

    def returnToMenu(self):
        self.sw.setCurrentIndex(0)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2 - 50)


