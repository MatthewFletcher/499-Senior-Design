from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QGroupBox,
                             QListView)
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt
import sys

intervalList = (("mean", "hello"), ("medium", "hello"), ("mode", "hello"))
ordinalList = (("mean", "hello"), ("medium", "hello"), ("mode", "hello"))
frequencyList = (("mean", "hello"), ("medium", "hello"), ("mode", "hello"))

class AnalysisTab(QWidget):
    def __init__(self):
        super().__init__()

        self.app = QApplication(sys.argv)
        self.screen = self.app.primaryScreen()
        self.size = self.screen.size()

        self.textWidth = self.size.width() * 0.45
        self.chooseWidth = self.size.width() * 0.49

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
        self.TextGroup = QGroupBox("Analysis")
        self.TextGroup.setFixedWidth(self.textWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # Here is where the analysis will go
        self.analysis = QLabel()

        self.layout = QGridLayout()
        self.layout.addWidget(self.analysis)
        self.TextGroup.setLayout(self.layout)

    # The right side of AnalysisTab containing the buttons for
    # analysis
    def createChooseGroup(self):
        self.ChooseGroup = QGroupBox("Tests")
        self.ChooseGroup.setFixedWidth(self.chooseWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # List widgets where users will choose what analysis
        # they would like ran on their data
        self.intervalAnalysis = QListView()
        self.ordinalAnalysis = QListView()
        self.frequencyAnalysis = QListView()

        self.model = QStandardItemModel()

        for test, function in intervalList:
            item = QStandardItem(test)
            item.setCheckable(True)
            check = Qt.Unchecked
            item.setCheckState(check)
            self.model.appendRow(item)

        self.intervalAnalysis.setModel(self.model)
        self.layout = QGridLayout()
        self.layout.addWidget(self.intervalAnalysis)
        self.ChooseGroup.setLayout(self.layout)
