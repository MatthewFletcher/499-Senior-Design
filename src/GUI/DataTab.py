from PyQt5.QtWidgets import (QApplication, QTabWidget, QDialog,
QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
QTextEdit, QLineEdit, QMainWindow, QFileDialog, QRadioButton, 
QGroupBox, QCheckBox, QPushButton, QGridLayout, QButtonGroup)
from PyQt5.QtGui import QIcon
from PyQt5 import Qt
import os
import csv
import sys 

class DataTab(QWidget):
    def __init__(self):
        super().__init__()

        self.createGraphGroup()
        self.createCustomGroup()

        layout = QGridLayout()
        layout.addWidget(self.GraphGroup, 0, 0, 0, 1)
        layout.addWidget(self.CustomGroup, 0, 1)
        #layout.addWidget(self.form_widget.openMadeSheet())
        self.setLayout(layout)
        self.show()

    def createGraphGroup(self):
        self.GraphGroup = QGroupBox("Group 1")

        self.form_widget = Table(100, 100)

        layout = QVBoxLayout()
        layout.addWidget(self.form_widget)
        self.GraphGroup.setLayout(layout)    

    def createCustomGroup(self):
        self.CustomGroup = QGroupBox()

        # Ask user what they'd like to graph
        graphLabel = QLabel("How much do you want graphed?")
        graphGroup = QButtonGroup()
        allRadioButton = QRadioButton("Graph everything")
        selectionRadioButton = QRadioButton("Let me pick what to graph")
        graphGroup.addButton(allRadioButton)
        graphGroup.addButton(selectionRadioButton)

        # Ask user what type of data it is 
        dataLabel = QLabel("What kind of data is it?")
        newLine = QLabel("\n")
        typeGroup = QButtonGroup()
        intervalRadioButton = QRadioButton("Interval")
        ordinalRadioButton = QRadioButton("Ordinal")
        frequencyRadioButton = QRadioButton("Frequency")
        typeGroup.addButton(intervalRadioButton)
        typeGroup.addButton(ordinalRadioButton)
        typeGroup.addButton(frequencyRadioButton)

        # Buttons to let the user submit the data
        goButton = QPushButton("Submit Data")
        goButton.setDefault(True)
        newButton = QPushButton("Import New CSV")
        newButton.setDefault(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(graphLabel)
        layout.addWidget(allRadioButton)
        layout.addWidget(selectionRadioButton)
        layout.addWidget(newLine)

        layout.addWidget(dataLabel)
        layout.addWidget(intervalRadioButton)
        layout.addWidget(ordinalRadioButton)
        layout.addWidget(frequencyRadioButton)
        layout.addStretch(1)
        layout.addWidget(newLine)

        layout.addWidget(goButton)
        layout.addWidget(newButton)
        layout.addStretch(1)
        self.CustomGroup.setLayout(layout) 

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
    
    def openBlankSheet(self):
        i = 2

    def openMadeSheet(self):
        self.checkChange = False
        path = QFileDialog.getOpenFileName(self, "Open CSV", os.getenv("HOME"), "CSV(*.csv)")
        if path[0] != '':
            with open(path[0], newline = '') as csv_file:
                self.setRowCount(0)
                self.setColumnCount(10)
                my_file = csv.reader(csv_file, delimiter = ',', quotechar = '|')
                for row_data in my_file:
                    row = self.rowCount()
                    self.insertRow(row)
                    if len(row_data) > 10:
                        self.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)

        self.checkChange = True