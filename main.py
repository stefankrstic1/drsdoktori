from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui
import sys, random

from menu import UI

class BubbleBobble(QMainWindow, UI):

    def __init__(self, parent=None):
        super(BubbleBobble, self).__init__(parent)
        self.init()
        self.initUI()
        self.btn.clicked.connect(self.openSinglePlay)
        self.btn1.clicked.connect(self.openMultiPlay)
        self.btn3.clicked.connect(self.exitoni)

    def openSinglePlay(self):
        self.StackedWidgets.setCurrentIndex(1)

    def openMultiPlay(self):
        self.StackedWidgets.setCurrentIndex(2)

    def exitoni(self):
        sys.exit()

    def initUI(self):
        self.setGeometry(0, 0, 1280, 960)
        self.setWindowTitle('BubbleBobble')
        self.setWindowIcon(QIcon('bb.jpg'))
        self.setFixedSize(1280,960)
        self.setCentralWidget(self.StackedWidgets)
        UI.center(self)

        self.show()

    def display(self):
        self.stackedWidgets.setCurrentIndex(0)

class AllWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

class SinglePlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        oImage = QImage("pozadina.jpg")
        sImage = oImage.scaled(QSize(640, 480))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bubbleBobble = BubbleBobble()
    sys.exit(app.exec_())