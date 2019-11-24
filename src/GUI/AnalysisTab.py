from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QGroupBox,
                             QListView, QPushButton)
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt
import sys, os
from pathlib import Path
import inspect

from scipy.stats import norm

foo = norm.a


sys.path.append(str(Path(os.getcwd()).joinpath("./src/csvtools").resolve()))
sys.path.append(str(Path(os.getcwd()).joinpath("./src/Math").resolve()))
sys.path.append(str(Path(os.getcwd()).joinpath("../Math").resolve()))
sys.path.append(str(Path(os.getcwd()).joinpath("../csvtools").resolve()))
sys.path.append(str(Path(os.path.abspath(__file__)).joinpath("../../Math").resolve()))
import Stats_Wizard as sw

from pandas import DataFrame

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
        self.mydata = None

        # These numbers are arbitrary and seemed
        # to have the best balance
        self.textWidth = self.size.width() * 0.64
        self.chooseWidth = self.size.width() * 0.29

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
        self.analysis2 = QLabel()

        self.layout = QGridLayout()
        self.layout.addWidget(self.analysis)
        self.layout.addWidget(self.analysis2)
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

        self.model = QStandardItemModel(self.intervalAnalysis)

        # for test, function in intervalList:
        tempdata = {'foo':[], 'bar':[]}
        df = DataFrame(tempdata, columns=["foo", 'bar'])
        ds = tempdata['foo']

        for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("s_")]:
            item = test(ds)
            item = QStandardItem(item.name)
            item.setCheckable(True)
            check = Qt.Unchecked
            item.setCheckState(check)
            self.model.appendRow(item)

        for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("r_")]:
            item = test(df)
            item = QStandardItem(item.name)
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

        self.model = QStandardItemModel(self.ordinalAnalysis)

        # for test, function in intervalList:
        tempdata = {'foo':[], 'bar':[]}
        df = DataFrame(tempdata, columns=["foo", 'bar'])
        ds = tempdata['foo']

        for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("s_")]:
            item = test(ds)
            item = QStandardItem(item.name)
            item.setCheckable(True)
            check = Qt.Unchecked
            item.setCheckState(check)
            self.model.appendRow(item)

        for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("r_")]:
            item = test(df)
            item = QStandardItem(item.name)
            item.setCheckable(True)
            check = Qt.Unchecked
            item.setCheckState(check)
            self.model.appendRow(item)


        print(self.model)
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

        self.model = QStandardItemModel(self.frequencyAnalysis)

        # for test, function in intervalList:
        tempdata = {'foo':[], 'bar':[]}
        df = DataFrame(tempdata, columns=["foo", 'bar'])
        ds = tempdata['foo']

        for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("s_")]:
            item = test(ds)
            item = QStandardItem(item.name)
            item.setCheckable(True)
            check = Qt.Unchecked
            item.setCheckState(check)
            self.model.appendRow(item)

        for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("r_")]:
            item = test(df)
            item = QStandardItem(item.name)
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
        elif dataType == "ordinal":
            self.analyzeIntervalButton.setEnabled(False)
            self.analyzeOrdinalButton.setEnabled(True)
            self.analyzeFrequencyButton.setEnabled(False)
        elif dataType == "frequency":
            self.analyzeIntervalButton.setEnabled(False)
            self.analyzeOrdinalButton.setEnabled(False)
            self.analyzeFrequencyButton.setEnabled(True)

    # Placeholders
    def intervalButtonClicked(self):
        df = sw.Regression(self.mydata)
        ds = sw.Statistics(self.mydata)
        rr = sw.Regression(df.df)
        sys.stderr.write("Print 1\n")
        currentSelection = self.intervalAnalysis.selectedIndexes()

        name = None
        row = None
        index = None

        # Set name for currently selected object in listview
        for obj_index in currentSelection:
            item = self.model.itemFromIndex(obj_index)
            row = item.row()
            index = self.model.index(row, 0)
            name = self.model.data(index)

        self.currName = name
        self.currRow = row
        self.currIndx = index

        print(self.currName)

        # for _ in select:
        #     sys.stderr.write("Print 1\n")
        #     for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("s_")]:
        #         temp = test(ds.d)
        #         self.textGroup.analysis.setText(f"Test: {temp.name}\nResult: {temp.func()}\n")
        #
        #     for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("r_")]:
        #         temp = test(rr.df)
        #         self.textGroup.analysis2 = f"Test: {temp.name}\nResult: {temp.func()}\n"

    def ordinalButtonClicked(self):
        df = self.mydata
        ds = sw.Statistics(self.mydata)
        for row in self.model:
            for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("s_")]:
                temp = test(ds.d)
                self.textGroup.analysis = f"Test: {temp.name}\nResult: {temp.func()}\n"

            for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("r_")]:
                temp = test(rr.df)
                self.textGroup.analysis2 = f"Test: {temp.name}\nResult: {temp.func()}\n"

    def frequencyButtonClicked(self):
        df = sw.Regression(self.mydata)
        ds = sw.Statistics(self.mydata)
        rr = sw.Regression(df.df)
        for row in self.model:
            for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("s_")]:
                temp = test(ds.d)
                self.textGroup.analysis = f"Test: {temp.name}\nResult: {temp.func()}\n"

            for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("r_")]:
                temp = test(rr.df)
                self.textGroup.analysis2 = f"Test: {temp.name}\nResult: {temp.func()}\n"
