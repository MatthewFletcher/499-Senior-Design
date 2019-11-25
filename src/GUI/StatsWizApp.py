from PyQt5.QtWidgets import (QApplication, QTabWidget, QVBoxLayout, QDesktopWidget, QDialog, QMainWindow)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys, os
from pathlib import Path
import WelcomeTab, DataTab, GraphTab, AnalysisTab, SummaryTab


class TabPage(QTabWidget):
    def __init__(self):

        super().__init__()
        self.setStyleSheet('font: 15pt Tw Cen MT')
        self.setWindowTitle("Stats Wiz")

        #Get directory name of this file
        #Get icon name from the generated absolute path
        self.setWindowIcon(QIcon(os.path.join(Path(os.path.dirname(os.path.abspath(__file__)),"StatsLogo1.png"))))
        #self.show()
        # Creating the tabs here to have a reference
        self.dataTab = DataTab.DataTab()
        self.graphTab = GraphTab.GraphTab()
        self.analysisTab = AnalysisTab.AnalysisTab()
        self.summaryTab = SummaryTab.SummaryTab()
        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(WelcomeTab.WelcomeTab(), "Welcome")
        self.tabWidget.addTab(self.dataTab, "Data Input")
        self.tabWidget.addTab(self.graphTab, "Graph")
        self.tabWidget.addTab(self.analysisTab, "Analysis")
        self.tabWidget.addTab(self.summaryTab, "Summary")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabWidget)
        self.setLayout(self.layout)
        self.dataTab.submitButton.clicked.connect(self.setDF)

    # This is a method of passing data from the data tab to the graph and/or analysis tab.
    def setDF(self):
        data = self.dataTab.getDataFromTable()
        print(data)
        self.graphTab.masterDF = data
        self.analysisTab.mydata = data
        self.graphTab.enableGraphType(self.dataTab.getDataType())

def runStatsWiz():
    app = QApplication(sys.argv)
    tabPage = TabPage()
    tabPage.show()
    app.exec_()


runStatsWiz()
