from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QGroupBox,
                             QListWidget)
import sys


class AnalysisTab(QWidget):
    def __init__(self):
        super().__init__()

        self.app = QApplication(sys.argv)
        self.screen = self.app.primaryScreen()
        self.size = self.screen.size()

        self.createTextGroup()
        self.createChooseGroup()

        self.layout = QGridLayout()
        self.layout.addWidget(self.TextGroup, 0, 0, 0, 1)
        self.layout.addWidget(self.ChooseGroup, 0, 1)
        self.setLayout(self.layout)
        self.show()

    # The left side of AnalysisTab containing the textbox
    # where the analysis will be shown
    def createTextGroup(self):
        self.TextGroup = QGroupBox()
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # Here is where the analysis will go
        self.analysis = QLabel()

        self.layout = QGridLayout()
        self.layout.addWidget(self.analysis)
        self.TextGroup.setLayout(self.layout)

    # The right side of AnalysisTab containing the buttons for
    # analysis
    def createChooseGroup(self):
        self.ChooseGroup = QGroupBox()
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # List widgets where users will choose what analysis
        # they would like ran on their data
        self.intervalAnalysis = QListWidget()
        self.ordinalAnalysis = QListWidget()
        self.frequencyAnalysis = QListWidget()

        self.intervalAnalysis.



        self.layout = QGridLayout()
        self.ChooseGroup.setLayout(self.layout)
