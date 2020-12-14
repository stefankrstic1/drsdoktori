from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import sys, random


class BubbleBobble(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 640, 480)
        self.setWindowTitle('BubbleBobble')
        self.setWindowIcon(QIcon('bb.jpg'))

        oImage = QImage("pozadina.jpg")
        sImage = oImage.scaled(QSize(640, 480))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        btn = QPushButton('PLAY', self)

        btn.setToolTip('Play the game')

        btn.resize(180, 60)
        btn.move(220, 240)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    bubbleBobble = BubbleBobble()
    sys.exit(app.exec_())