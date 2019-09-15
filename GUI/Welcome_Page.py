from PyQt5.QtWidgets import (QApplication,
QLabel,  QPushButton, QGridLayout, QWidget, 
QVBoxLayout, QGroupBox)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import sys

class StartPage(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Stats Wiz Start Page"
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 1000
        self.initUi()

    def initUi(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("StatsLogo1.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()

        windowLayout = QVBoxLayout()
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        layout = QGridLayout()

        pixmap = QPixmap("StatsLogo1.png")

        label = QLabel(self)
        label.setPixmap(pixmap)

        labelText = QLabel(self)
        labelText.setText("Welcome to the Stats Wiz!\n\nGet started by selecting\nhow you want to input your data.")
        labelText.setAlignment(Qt.AlignCenter)
        labelText.setStyleSheet("font: 20pt Tw Cen MT")

        layout.addWidget(QPushButton("Import CSV File"), 1, 1)
        layout.addWidget(QPushButton("Manual Input"), 2, 1)
        layout.addWidget(labelText, 0, 1)
        layout.addWidget(label, 0, 0)
        self.setLayout(layout)


    
app = QApplication(sys.argv)
startPage = StartPage()
startPage.show()
app.exec()