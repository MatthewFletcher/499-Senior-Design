from PyQt5.QtWidgets import (QApplication, QTabWidget, QDialog,
QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
QTextEdit, QLineEdit, QMainWindow, QFileDialog, QTabBar,
QDesktopWidget)
from PyQt5.QtGui import QIcon
import os
import csv
import sys 
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
    app = QApplication(sys.argv)
    tabPage = TabPage()
    tabPage.show()
    app.exec()

runStatsWiz()
