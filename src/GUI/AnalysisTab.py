from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QGroupBox,
                             QListView, QPushButton)
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt
import sys, os
from pathlib import Path
sys.path.append(str(Path(os.getcwd()).joinpath("./src/csvtools").resolve()))
sys.path.append(str(Path(os.getcwd()).joinpath("./src/Math").resolve()))

sys.path.append(str(Path(os.getcwd()).joinpath("../csvtools").resolve()))
sys.path.append(str(Path(os.getcwd()).joinpath("../Math").resolve()))
import Stats_Wizard as s

# The AnalysisTab class holds the GUI for the AnalysisTab, which consists of four sections:
# TextGroup, ChooseIntervalGroup, ChooseOrdinalGroup, and ChooseFrequencyGroup. The TextGroup
# prints out the analysis. The ChooseIntervalGroup allows the user to select the tests they
# wish to run on their interval data. The ChooseOrdinalGroup allows the user to select the
# tests they wish to run on their ordinal data. The ChooseFrequency group allows the user to
# select the tests they wish to run on their frequency data.
class AnalysisTab(QWidget):
    def __init__(self):
        
        super().__init__()
        self.app = QApplication(sys.argv)
        self.screen = self.app.primaryScreen()
        self.size = self.screen.size()

        # These numbers are arbitrary and seemed
        # to have the best balance
        self.textWidth = self.size.width() * 0.65
        self.chooseWidth = self.size.width() * 0.3

        self.createTextGroup()
        self.createChooseIntervalGroup()
        self.createChooseOrdinalGroup()
        self.createChooseFrequencyGroup()

        self.layout = QGridLayout()
        self.layout.addWidget(self.TextGroup, 0, 0, 0, 1)
        self.layout.addWidget(self.ChooseIntervalGroup, 0, 1)
        self.layout.addWidget(self.ChooseOrdinalGroup, 1, 1)
        self.layout.addWidget(self.ChooseFrequencyGroup, 2, 1)
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

    # The right side of AnalysisTab containing a checklist of tests that
    # may be run on the data and a button to press to run the tests
    def createChooseIntervalGroup(self):
        self.ChooseIntervalGroup = QGroupBox("Tests for Interval Data")
        self.ChooseIntervalGroup.setFixedWidth(self.chooseWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # List widgets where users will choose what analysis
        # they would like ran on their data
        self.intervalAnalysis = QListView()

        self.model = QStandardItemModel()

        # for test, function in intervalList:
        for test, function in s.Statistics(0).test_list():
            item = QStandardItem(test)
            item.setCheckable(True)
            check = Qt.Unchecked
            item.setCheckState(check)
            self.model.appendRow(item)

        self.analyzeIntervalButton = QPushButton("Analyze")
        self.analyzeIntervalButton.setEnabled(False)
        self.analyzeIntervalButton.clicked.connect(self.intervalButtonClicked)

        self.intervalAnalysis.setModel(self.model)
        self.layout = QGridLayout()
        self.layout.addWidget(self.intervalAnalysis, 0, 0, 0, 1)
        self.layout.addWidget(self.analyzeIntervalButton, 1, 1)
        self.ChooseIntervalGroup.setLayout(self.layout)

    # The right side of AnalysisTab containing a checklist of tests that
    # may be run on the data and a button to press to run the tests
    def createChooseOrdinalGroup(self):
        self.ChooseOrdinalGroup = QGroupBox("Tests for Ordinal Data")
        self.ChooseOrdinalGroup.setFixedWidth(self.chooseWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # List widgets where users will choose what analysis
        # they would like ran on their data
        self.ordinalAnalysis = QListView()

        self.model = QStandardItemModel()

        # for test, function in ordinalList:
        for test, function in s.Statistics(0).test_list():
            item = QStandardItem(test)
            item.setCheckable(True)
            check = Qt.Unchecked
            item.setCheckState(check)
            self.model.appendRow(item)

        self.analyzeOrdinalButton = QPushButton("Analyze")
        self.analyzeOrdinalButton.setEnabled(False)
        self.analyzeOrdinalButton.clicked.connect(self.ordinalButtonClicked)

        self.ordinalAnalysis.setModel(self.model)
        self.layout = QGridLayout()
        self.layout.addWidget(self.ordinalAnalysis, 0, 0, 0, 1)
        self.layout.addWidget(self.analyzeOrdinalButton, 1, 1)
        self.ChooseOrdinalGroup.setLayout(self.layout)

    # The right side of AnalysisTab containing a checklist of tests that
    # may be run on the data and a button to press to run the tests
    def createChooseFrequencyGroup(self):
        self.ChooseFrequencyGroup = QGroupBox("Tests for Frequency Data")
        self.ChooseFrequencyGroup.setFixedWidth(self.chooseWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # List widgets where users will choose what analysis
        # they would like ran on their data
        self.frequencyAnalysis = QListView()

        self.model = QStandardItemModel()

        # for test, function in frequencyList:
        for test, function in s.Statistics(0).test_list():
            item = QStandardItem(test)
            item.setCheckable(True)
            check = Qt.Unchecked
            item.setCheckState(check)
            self.model.appendRow(item)

        self.analyzeFrequencyButton = QPushButton("Analyze")
        self.analyzeFrequencyButton.setEnabled(False)
        self.analyzeFrequencyButton.clicked.connect(self.frequencyButtonClicked)

        self.frequencyAnalysis.setModel(self.model)
        self.layout = QGridLayout()
        self.layout.addWidget(self.frequencyAnalysis, 0, 0, 0, 1)
        self.layout.addWidget(self.analyzeFrequencyButton, 1, 1)
        self.ChooseFrequencyGroup.setLayout(self.layout)

    # Change the types of tests available depending on which
    # data type radio button is selected on DataTab
    def enableAnalysis(self, dataType):
        if dataType == "interval":
            self.analyzeIntervalButton.setEnabled(True)
            self.analyzeOrdinalButton.setEnabled(False)
            self.analyzeFrequencyButton.setEnabled(False)
        elif dataType == "frequency":
            self.analyzeIntervalButton.setEnabled(False)
            self.analyzeOrdinalButton.setEnabled(True)
            self.analyzeFrequencyButton.setEnabled(False)
        elif dataType == "ordinal":
            self.analyzeIntervalButton.setEnabled(False)
            self.analyzeOrdinalButton.setEnabled(False)
            self.analyzeFrequencyButton.setEnabled(True)

    # Placeholders
    def intervalButtonClicked(self):
        y = 0

    def ordinalButtonClicked(self):
        y = 0

    def frequencyButtonClicked(self):
        y = 0