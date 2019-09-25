from PyQt5.QtWidgets import (QApplication, QTabWidget, QDialog,
QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
QTextEdit, QLineEdit, QMainWindow, QFileDialog, QRadioButton, 
QGroupBox, QCheckBox, QPushButton, QGridLayout)
from PyQt5.QtGui import QIcon
from PyQt5 import Qt
import os
import csv
import sys 

class DataTab(QWidget):
    def __init__(self):
        super().__init__()

        self.createGraphGroup()
        self.createSelectionGroup()
        self.createDataTypeGroup()

        layout = QGridLayout()
        layout.addWidget(self.LeftGroupBox, 0, 0)
        layout.addWidget(self.RightGroupBox, 0, 1)
        layout.addWidget(self.DataTypeGroup, 1, 1)
        #layout.addWidget(self.form_widget.openMadeSheet())
        self.setLayout(layout)
        self.show()

    def createGraphGroup(self):
        self.LeftGroupBox = QGroupBox("Group 1")

        self.form_widget = Table(100, 100)

        layout = QVBoxLayout()
        layout.addWidget(self.form_widget)
        self.LeftGroupBox.setLayout(layout)    

    def createSelectionGroup(self):
        self.RightGroupBox = QGroupBox("Do you want to analyze all your data or only part of it?")

        defaultPushButton = QPushButton("Default Push Button")
        defaultPushButton.setDefault(True)

        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        flatPushButton = QPushButton("Flat Push Button")
        flatPushButton.setFlat(True)

        layout = QVBoxLayout()
        layout.addWidget(defaultPushButton)
        layout.addWidget(togglePushButton)
        layout.addWidget(flatPushButton)
        layout.addStretch(1)
        self.RightGroupBox.setLayout(layout)

    def createDataTypeGroup(self):
        self.DataTypeGroup = QGroupBox("What Type of data is it?")

        radioButton1 = QRadioButton("Interval")
        radioButton2 = QRadioButton("Ordinal")
        radioButton3 = QRadioButton("Frequency")

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addStretch(1)
        self.DataTypeGroup.setLayout(layout) 



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