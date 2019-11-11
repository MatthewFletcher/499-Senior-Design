from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QTabWidget, QVBoxLayout)
from PyQt5.QtGui import QIcon
import sys, os
from pathlib import Path
import WelcomeTab, DataTab, GraphTab, AnalysisTab, SummaryTab


class TabPage(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('font: 15pt Tw Cen MT')
        self.setWindowTitle("Stats Wiz")
        self.setWindowIcon(QIcon("StatsLogo1.png"))
        self.show()
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

        # This checks to see which of the data type radio buttons on the DataTab
        # are checked. If the interval radio button is checked, then the only
        # button available on AnalysisTab is for the interval data type
        self.dataTab.intervalRadioButton.toggled.connect(
            self.analysisTab.analyzeIntervalButton.setEnabled
        )
        self.dataTab.ordinalRadioButton.toggled.connect(
            self.analysisTab.analyzeOrdinalButton.setEnabled
        )
        self.dataTab.frequencyRadioButton.toggled.connect(
            self.analysisTab.analyzeFrequencyButton.setEnabled
        )

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tabWidget)
        self.setLayout(self.layout)
        self.dataTab.submitButton.clicked.connect(self.setDF)

    # This function is being called when the user clicks the "Submit Data" in the data tab.
    # This is a method of passing data from the data tab to the graph tab.
    def setDF(self, df):
        self.graphTab.masterDF = self.dataTab.getDataFromTable()
        self.graphTab.enableGraphType(self.dataTab.getDataType())

def runStatsWiz():
    app = QApplication(sys.argv)
    tabPage = TabPage()
    tabPage.show()
    app.exec_()


runStatsWiz()
