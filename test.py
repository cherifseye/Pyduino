from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMainWindow, QFrame, QLabel, QHBoxLayout, QLineEdit, QComboBox
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QIcon
import sys


class MainWin(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.UI()
        self.partie1()
        self.partie2()

    def initUI(self):
        self.setWindowTitle('PyQt5 GUI')
        self.setGeometry(300, 300, 300, 200)

    def UI(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.hlayoutgen = QHBoxLayout(self.centralWidget)
        self.hlayoutgen.setObjectName("hlayoutgen")

    def partie1(self):
        self.fram1 = QFrame(self.centralWidget)
        self.fram1.setObjectName("fram1")
        self.fram1.setFrameShape(QFrame.StyledPanel)
        self.fram1.setFrameShadow(QFrame.Raised)
        self.hlayoutgen.addWidget(self.fram1)

        self.framm1 = QFrame(self.fram1)
        self.framm1.setObjectName("framm1")
        self.framm1.setFrameShape(QFrame.StyledPanel)
        self.framm1.setFrameShadow(QFrame.Raised)

        self.framm2 = QFrame(self.fram1)
        self.framm2.setObjectName("framm2")
        self.framm2.setFrameShape(QFrame.StyledPanel)
        self.framm2.setFrameShadow(QFrame.Raised)

        self.layver1 = QVBoxLayout(self.fram1)
        self.layver1.setObjectName("layver1")
        self.layver1.addWidget(self.framm1)
        self.layver1.addWidget(self.framm2)


    def partie2(self):
        self.fram2 = QFrame(self.centralWidget)
        self.fram2.setObjectName("fram2")
        self.fram2.setFrameShape(QFrame.StyledPanel)
        self.fram2.setFrameShadow(QFrame.Raised)
        self.hlayoutgen.addWidget(self.fram2)
    


def main():
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()