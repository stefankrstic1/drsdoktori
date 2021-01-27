from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui,QtWidgets,QtCore

class Labels:
    def __init__(self, screen: QWidget):
        self.label = QtWidgets.QLabel(screen)
        self.label.setGeometry(QtCore.QRect(10,20,100,35))
        self.label.setStyleSheet('background-image: url()')
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("SCORE:")

        self.points = 0

        self.label_2 = QtWidgets.QLabel(screen)
        self.label_2.setGeometry(QtCore.QRect(10, 39, 55, 100))
        self.label_2.setStyleSheet('background-image: url()')
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label2")
        self.label_2.setNum(self.points)

    def changeScore(self, pts):
        self.points = pts
        self.label_2.setNum(self.points)