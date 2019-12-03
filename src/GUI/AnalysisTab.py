from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QGroupBox,
                             QListView, QPushButton, QTextEdit)
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt
import sys, os
from pathlib import Path
import inspect
import logging
from scipy.stats import norm
import traceback

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
        self.createStatsGroup()
        self.createRegGroup()

        self.layout = QGridLayout()
        self.layout.addWidget(self.TextGroup, 0, 0, 0, 1)
        self.layout.addWidget(self.StatsGroup, 0, 1)
        self.layout.addWidget(self.RegGroup, 1, 1)
        self.setLayout(self.layout)
        self.show()

    # The left side of AnalysisTab containing the textbox
    # where the analysis will be shown
    def createTextGroup(self):
        self.TextGroup = QGroupBox("Analysis")
        self.TextGroup.setFixedWidth(self.textWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # Here is where the analysis will go
        self.analysis = QTextEdit()

        self.layout = QGridLayout()
        self.layout.addWidget(self.analysis)
        self.TextGroup.setLayout(self.layout)

    # The right side of AnalysisTab containing a checklist of tests that
    # may be run on the data and a button to press to run the tests
    def createStatsGroup(self):
        self.StatsGroup = QGroupBox("Statistics Tests")
        self.StatsGroup.setFixedWidth(self.chooseWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # List widgets where users will choose what analysis
        # they would like ran on their data
        self.statsAnalysis = QListView()
        self.modelStats = QStandardItemModel(self.statsAnalysis)

        # for test, function in intervalList:
        tempdata = {'foo': [], 'bar': []}
        df = DataFrame(tempdata, columns=["foo", 'bar'])
        ds = tempdata['foo']

        for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("s_")]:
            item = test(ds)
            item = QStandardItem(item.name)
            item.setCheckable(False)
            item.setEnabled(False)
            check = Qt.Unchecked
            item.setCheckState(check)
            self.modelStats.appendRow(item)

        self.statsButton = QPushButton("Analyze")
        self.statsButton.setEnabled(False)
        self.statsButton.clicked.connect(self.statsButtonClicked)

        self.statsAnalysis.setModel(self.modelStats)
        self.layout = QGridLayout()
        self.layout.addWidget(self.statsAnalysis, 0, 0, 0, 1)
        self.layout.addWidget(self.statsButton, 1, 1)
        self.StatsGroup.setLayout(self.layout)

    # The right side of AnalysisTab containing a checklist of tests that
    # may be run on the data and a button to press to run the tests
    def createRegGroup(self):
        self.RegGroup = QGroupBox("Regression Tests")
        self.RegGroup.setFixedWidth(self.chooseWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # List widgets where users will choose what analysis
        # they would like ran on their data
        self.regAnalysis = QListView()

        self.modelReg = QStandardItemModel(self.regAnalysis)

        # for test, function in intervalList:
        tempdata = {'foo': [], 'bar': []}
        df = DataFrame(tempdata, columns=["foo", 'bar'])
        ds = tempdata['foo']

        for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("r_")]:
            item = test(df)
            item = QStandardItem(item.name)
            item.setCheckable(False)
            item.setEnabled(False)
            check = Qt.Unchecked
            item.setCheckState(check)
            self.modelReg.appendRow(item)

        self.regButton = QPushButton("Analyze")
        self.regButton.setEnabled(False)
        self.regButton.clicked.connect(self.regButtonClicked)

        self.regAnalysis.setModel(self.modelReg)
        self.layout = QGridLayout()
        self.layout.addWidget(self.regAnalysis, 0, 0, 0, 1)
        self.layout.addWidget(self.regButton, 1, 1)
        self.RegGroup.setLayout(self.layout)

    # Change the types of tests available depending on which
    # data type radio button is selected on DataTab
    def enableStatistics(self, dataType):
        self.statsButton.setEnabled(True)
        self.regButton.setEnabled(False)
        ds = self.mydata
        count = 0

        for index in range(self.modelStats.rowCount()):
            item = self.modelStats.item(index)
            item.setCheckable(False)
            item.setEnabled(False)
            item.setCheckState(False)

        for index in range(self.modelReg.rowCount()):
            item = self.modelReg.item(index)
            item.setCheckable(False)
            item.setEnabled(False)
            item.setCheckState(False)

        if dataType == "interval":
            for index in range(self.modelStats.rowCount()):
                item = self.modelStats.item(index)
                for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("s_")]:
                    temp = test(ds)
                    if 'i' in temp.validTests and count == index:
                        item.setCheckable(True)
                        item.setEnabled(True)
                        count += 1

        elif dataType == "ordinal":
            for index in range(self.modelStats.rowCount()):
                item = self.modelStats.item(index)
                for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("s_")]:
                    temp = test(ds)
                    if 'o' in temp.validTests and count == index:
                        item.setCheckable(True)
                        item.setEnabled(True)
                        count += 1

        elif dataType == "frequency":
            for index in range(self.modelStats.rowCount()):
                item = self.modelStats.item(index)
                for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("s_")]:
                    temp = test(ds)
                    if 'f' in temp.validTests and count == index:
                        item.setCheckable(True)
                        item.setEnabled(True)
                        count += 1

    # Change the types of tests available depending on which
    # data type radio button is selected on DataTab
    def enableRegession(self, dataType):
        self.statsButton.setEnabled(False)
        self.regButton.setEnabled(True)
        ds = self.mydata
        count = 0

        for index in range(self.modelReg.rowCount()):
            item = self.modelReg.item(index)
            item.setCheckable(False)
            item.setEnabled(False)
            item.setCheckState(False)

        for index in range(self.modelStats.rowCount()):
            item = self.modelStats.item(index)
            item.setCheckable(False)
            item.setEnabled(False)
            item.setCheckState(False)

        if dataType == "interval":
            for index in range(self.modelReg.rowCount()):
                item = self.modelReg.item(index)
                for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("r_")]:
                    temp = test(ds)
                    if 'i' in temp.validTests and count == index:
                        item.setCheckable(True)
                        item.setEnabled(True)
                        count += 1

        elif dataType == "ordinal":
            for index in range(self.modelReg.rowCount()):
                item = self.modelReg.item(index)
                for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("r_")]:
                    temp = test(ds)
                    if 'o' in temp.validTests and count == index:
                        item.setCheckable(True)
                        item.setEnabled(True)
                        count += 1

        elif dataType == "frequency":
            for index in range(self.modelReg.rowCount()):
                item = self.modelReg.item(index)
                for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith("r_")]:
                    temp = test(ds)
                    if 'f' in temp.validTests and count == index:
                        item.setCheckable(True)
                        item.setEnabled(True)
                        count += 1

    def statsButtonClicked(self):
        ds = self.mydata
        checked_options = []
        count = 0
        for index in range(self.modelStats.rowCount()):
            item = self.modelStats.item(index)
            for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith('s_')]:
                temp = test(ds)
                if item.checkState() == Qt.Checked and count == index:
                    checked_options.append(f"Test: {temp.name}\nResult:{'No Result' if temp.func() is None else temp.func()}\n")
                    logging.info(f"Test: {temp.name}\nResult:{'No Result' if temp.func() is None else temp.func()}\n")
                    count += 1
                    break
                else:
                    count += 1
            count = 0

        if checked_options:
            self.analysis.setText("\n".join(checked_options))
        logging.info('-------------------------------------------------------------------------------------------\n')

    def regButtonClicked(self):
        df = self.mydata
        checked_options = []
        count = 0
        for index in range(self.modelReg.rowCount()):
            item = self.modelReg.item(index)
            for _, test in [m for m in inspect.getmembers(sw) if m[0].startswith('r_')]:
                temp = test(df)
                if item.checkState() == Qt.Checked and count == index:
                    checked_options.append(f"Test: {temp.name}\nResult: {temp.func()}\n")
                    logging.info(f"Test: {temp.name}\nResult: {temp.func()}\n")
                    count += 1
                    break
                else:
                    count += 1
            count = 0

        if checked_options:
            self.analysis.setText("\n".join(checked_options))
        logging.info('-------------------------------------------------------------------------------------------\n')
