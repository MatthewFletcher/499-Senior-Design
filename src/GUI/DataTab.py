from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
                             QLineEdit, QFileDialog, QRadioButton,QGroupBox,QPushButton,
                             QGridLayout, QButtonGroup)
from PyQt5.QtGui import QIcon
#from PyQt5 import Qt
import os
import csv
import sys


class DataTab(QWidget):
    def __init__(self):
        super().__init__()

        self.createGraphGroup()
        self.createCustomGroup()

        self.layout = QGridLayout()
        self.layout.addWidget(self.GraphGroup, 0, 0, 0, 1)
        self.layout.addWidget(self.CustomGroup, 0, 1)
        # layout.addWidget(self.form_widget.openMadeSheet())
        self.setLayout(self.layout)
        self.show()

    def createGraphGroup(self):
        self.GraphGroup = QGroupBox()

        self.form_widget = Table(1000, 1000)

        self.GraphGroup.setFixedWidth(1800)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.form_widget)
        self.GraphGroup.setLayout(self.layout)

    def createCustomGroup(self):
        self.CustomGroup = QGroupBox()

        # Ask user what they'd like to graph
        self.graphLabel = QLabel("How much do you want graphed?")
        self.graphGroup = QButtonGroup()
        self.allRadioButton = QRadioButton("Graph everything")
        self.selectionRadioButton = QRadioButton("Let me pick what to graph")
        self.graphGroup.addButton(self.allRadioButton)
        self.graphGroup.addButton(self.selectionRadioButton)

        self.beginRow = QLineEdit()
        self.beginCol = QLineEdit()
        self.endRow = QLineEdit()
        self.endCol = QLineEdit()
        self.beginRow.setFixedWidth(100)
        self.beginCol.setFixedWidth(100)
        self.endRow.setFixedWidth(100)
        self.endCol.setFixedWidth(100)

        # Ask user what type of data it is 
        self.dataLabel = QLabel("What kind of data is it?")
        self.newLine = QLabel("\n")
        self.typeGroup = QButtonGroup()
        self.intervalRadioButton = QRadioButton("Interval")
        self.ordinalRadioButton = QRadioButton("Ordinal")
        self.frequencyRadioButton = QRadioButton("Frequency")
        self.typeGroup.addButton(self.intervalRadioButton)
        self.typeGroup.addButton(self.ordinalRadioButton)
        self.typeGroup.addButton(self.frequencyRadioButton)

        # Buttons to let the user submit the data
        self.newCSVButton = QPushButton("Import CSV")
        self.newCSVButton.setDefault(True)
        self.newCSVButton.setFixedWidth(400)
        self.clearButton = QPushButton("Clear Table")
        self.clearButton.setDefault(True)
        self.clearButton.setFixedWidth(400)
        self.goButton = QPushButton("Submit Data")
        self.goButton.setDefault(True)
        self.goButton.setFixedWidth(400)

        # Layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.graphLabel)
        self.layout.addWidget(self.allRadioButton)
        self.layout.addWidget(self.selectionRadioButton)
        self.layout.addWidget(self.beginRow)
        self.layout.addWidget(self.beginCol)
        self.layout.addWidget(self.endRow)
        self.layout.addWidget(self.endCol)
        self.layout.addWidget(self.newLine)

        self.layout.addWidget(self.dataLabel)
        self.layout.addWidget(self.intervalRadioButton)
        self.layout.addWidget(self.ordinalRadioButton)
        self.layout.addWidget(self.frequencyRadioButton)
        self.layout.addStretch(1)
        self.layout.addWidget(self.newLine)

        self.layout.addWidget(self.newCSVButton)
        self.layout.addWidget(self.clearButton)
        self.layout.addWidget(self.goButton)
        self.layout.addStretch(1)
        self.CustomGroup.setAlignment(100)
        self.CustomGroup.setLayout(self.layout)


class Table(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.checkChange = True
        self.initUi()

    def initUi(self):
        self.cellChanged.connect(self.currentCell)
        self.show()

    def currentCell(self):
        if self.checkChange:
            row = self.currentRow()
            col = self.currentColumn()
            value = self.item(row, col)
            value = value.text()

    # def openBlankSheet(self):
    #     i = 2

    def openMadeSheet(self):
        self.checkChange = False
        path = QFileDialog.getOpenFileName(self, "Open CSV", os.getenv("HOME"), "CSV(*.csv)")
        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                self.setRowCount(0)
                self.setColumnCount(10)
                my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    row = self.rowCount()
                    self.insertRow(row)
                    if len(row_data) > 10:
                        self.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)

        self.checkChange = True
