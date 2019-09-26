from PyQt5.QtWidgets import (QApplication,
QLabel,  QPushButton, QGridLayout, QWidget, 
QVBoxLayout, QGroupBox, QDesktopWidget, QTabBar,
QMainWindow, QTabWidget)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
import sys
#import StatsWizApp

class StartPage(QMainWindow):
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

        importButton = QPushButton("Import CSV File")
        manualButton = QPushButton("Manual Input")

        importButton.setIconSize(QSize(20, 20))   
        importButton.setStyleSheet("font: 18pt Tw Cen MT")

        manualButton.setIconSize(QSize(20, 20))   
        manualButton.setStyleSheet("font: 18pt Tw Cen MT")

        importButton.clicked.connect(self.importClick)
        manualButton.clicked.connect(self.manualClick)

        layout.addWidget(importButton, 1, 1)
        layout.addWidget(manualButton, 2, 1)
        layout.addWidget(labelText, 0, 1)
        layout.addWidget(label, 0, 0)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(layout)

    def importClick(self):
        self.close()
        tabPage = TabPage()
        tabPage.show()

    def manualClick(self):
        self.close()
        TabPage().show()

def main():
    welcomeApp = QApplication(sys.argv)
    startPage = StartPage()
    startPage.show()
    welcomeApp.exec()

main()

import DataTab, GraphTab, AnalysisTab, SummaryTab

class TabPage(QTabWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet('font: 15pt Tw Cen MT')

        self.setWindowTitle("Stats Wiz")
        self.setWindowIcon(QIcon("StatsLogo1.png"))
        self.left = 20
        self.top = 20
        self.width = 2600
        self.height = 1300

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

        tabwidget = QTabWidget()
        tabwidget.addTab(DataTab.DataTab(), "Data Input")
        tabwidget.addTab(GraphTab.GraphTab(), "Graph")
        tabwidget.addTab(AnalysisTab.AnalysisTab(), "Analysis")
        tabwidget.addTab(SummaryTab.SummaryTab(), "Summary")

        layout = QVBoxLayout()
        layout.addWidget(tabwidget)
        self.setLayout(layout)

def runStatsWiz():
    #app = QApplication(sys.argv)
    tabPage = TabPage()
    tabPage.show()
    #app.exec()