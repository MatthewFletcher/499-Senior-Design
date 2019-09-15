from PyQt5.QtWidgets import (QApplication,
QLabel,  QPushButton, QGridLayout, QWidget, 
QVBoxLayout, QGroupBox)
from PyQt5.QtGui import QPixmap, QIcon
import sys

class StartPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("StatsLogo1.png"))
        self.title = "Stats Wiz Start Page"
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 1000
        self.initUi()

    def initUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()

        windowLayout = QVBoxLayout()
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)

        pixmap = QPixmap("StatsLogo1.png")

        label = QLabel(self)
        label.setPixmap(pixmap)

        layout.addWidget(QPushButton("Import CSV File"), 2, 2)
        layout.addWidget(QPushButton("Manual Input"), 2, 3)
        layout.addWidget(label, 1, 1)
        self.setLayout(layout)


    
app = QApplication(sys.argv)
startPage = StartPage()
startPage.show()
app.exec()