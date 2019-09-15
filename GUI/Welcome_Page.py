from PyQt5.QtWidgets import (QApplication,
QLabel,  QPushButton, QGridLayout, QWidget, 
QVBoxLayout, QGroupBox)
from PyQt5.QtGui import QPixmap
import sys

class StartPage(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Stats Wiz Start Page"
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 500
        self.initUi()

    def initUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()

        pixmap = QPixmap("StatsLogo1.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(lbl)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        layout.addWidget(QPushButton("Import CSV File"), 2, 2)
        layout.addWidget(QPushButton("Manual Input"), 2, 3)
        self.setLayout(layout)


    
app = QApplication(sys.argv)
startPage = StartPage()
startPage.show()
app.exec()