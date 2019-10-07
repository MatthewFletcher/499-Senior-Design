from PyQt5.QtWidgets import (QApplication, QTabWidget, QDialog,
                             QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
                             QTextEdit, QLineEdit, QMainWindow, QFileDialog, QTabBar,
                             QDesktopWidget)
from PyQt5.QtGui import QIcon
import sys
import csv
import os
import WelcomeTab, DataTab, GraphTab, AnalysisTab, SummaryTab


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

        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(WelcomeTab.WelcomeTab(), "Welcome")
        self.tabWidget.addTab(DataTab.DataTab(), "Data Input")
        self.tabWidget.addTab(GraphTab.GraphTab(), "Graph")
        self.tabWidget.addTab(AnalysisTab.AnalysisTab(), "Analysis")
        self.tabWidget.addTab(SummaryTab.SummaryTab(), "Summary")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabWidget)
        self.setLayout(self.layout)


def runStatsWiz():
    app = QApplication(sys.argv)
    tabPage = TabPage()
    tabPage.show()
    app.exec_()


runStatsWiz()
