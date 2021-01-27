from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui
import sys, random
import winsound
import sys, random, variables

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
        filename = 'resources/bgm/muzika.wav'
        #winsound.PlaySound(filename, winsound.SND_ASYNC)
        variables.gameLive = True

    def openMultiPlay(self):
        self.StackedWidgets.setCurrentIndex(2)

    def exitoni(self):
        sys.exit()

    def initUI(self):
        self.setGeometry(0, 0, 1280, 960)
        self.setWindowTitle('Slike/BubbleBobble')
        self.setWindowIcon(QIcon('bb.jpg'))
        self.setFixedSize(1280,960)
        self.setCentralWidget(self.StackedWidgets)
        UI.center(self)

        self.show()

    def display(self):
        self.stackedWidgets.setCurrentIndex(0)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    bubbleBobble = BubbleBobble()
    sys.exit(app.exec_())