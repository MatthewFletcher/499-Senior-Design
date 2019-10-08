from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
                             QLineEdit, QFileDialog, QRadioButton, QGroupBox, QPushButton,
                             QGridLayout, QButtonGroup)
import os
import csv
from qtpy import QtGui


# The DataTab class holds all the GUI for the DataTab
class DataTab(QWidget):
    def __init__(self):
        super().__init__()

        self.createTableGroup()
        self.createCustomGroup()

        self.layout = QGridLayout()
        self.layout.addWidget(self.TableGroup, 0, 0, 0, 1)
        self.layout.addWidget(self.CustomGroup, 0, 1)
        self.setLayout(self.layout)
        self.show()

# The left side of DataTab containing the Table
    def createTableGroup(self):
        self.TableGroup = QGroupBox()

        self.myTable = QTableWidget(400, 400)

        self.TableGroup.setFixedWidth(1750)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.myTable)
        self.TableGroup.setLayout(self.layout)

# The right side of DataTab containing Radio Buttons and
# text boxes for user input on how they want their graph
    def createCustomGroup(self):
        self.CustomGroup = QGroupBox()
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # Ask user what they'd like to graph
        self.graphLabel = QLabel("How much do you want graphed?")
        self.graphGroup = QButtonGroup()
        self.allRadioButton = QRadioButton("Graph everything")
        self.selectionRadioButton = QRadioButton("Let me pick what to graph")
        self.graphGroup.addButton(self.allRadioButton)
        self.graphGroup.addButton(self.selectionRadioButton)
        self.allRadioButton.toggled.connect(self.allRadioButtonClicked)
        self.selectionRadioButton.toggled.connect(self.selectionRadioButtonClicked)

        # Space for users to input the rows and columns
        # they want graphed
        self.beginRowText = QLabel("Start Row: ")
        self.beginColText = QLabel("Start Col: ")
        self.endRowText = QLabel("End Row: ")
        self.endColText = QLabel("End Col: ")

        self.beginRow = QLineEdit()
        self.beginCol = QLineEdit()
        self.endRow = QLineEdit()
        self.endCol = QLineEdit()
        self.beginRow.setFixedWidth(150)
        self.beginCol.setFixedWidth(150)
        self.endRow.setFixedWidth(150)
        self.endCol.setFixedWidth(150)

        # Have the QLineEdits only be editable if
        # selectionRadioButton is selected
        self.beginRow.setReadOnly(True)
        self.beginCol.setReadOnly(True)
        self.endRow.setReadOnly(True)
        self.endCol.setReadOnly(True)

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
        self.newCSVButton.setFixedWidth(680)
        self.newCSVButton.clicked.connect(self.newCSVButtonClicked)

        self.clearButton = QPushButton("Clear Table")
        self.clearButton.setDefault(True)
        self.clearButton.setFixedWidth(680)


        self.goButton = QPushButton("Submit Data")
        self.goButton.setDefault(True)
        self.goButton.setFixedWidth(680)

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.graphLabel, 0, 0, 1, 4)
        self.layout.addWidget(self.allRadioButton, 1, 0, 1, 3)
        self.layout.addWidget(self.selectionRadioButton, 2, 0, 1, 3)
        self.layout.addWidget(self.beginRowText, 3, 0)
        self.layout.addWidget(self.beginRow, 3, 1)
        self.layout.addWidget(self.beginColText, 3, 2)
        self.layout.addWidget(self.beginCol, 3, 3)
        self.layout.addWidget(self.endRowText, 4, 0)
        self.layout.addWidget(self.endRow, 4, 1)
        self.layout.addWidget(self.endColText, 4, 2)
        self.layout.addWidget(self.endCol, 4, 3)
        self.layout.addWidget(self.newLine, 5, 0, 1, 3)

        self.layout.addWidget(self.dataLabel, 6, 0, 1, 3)
        self.layout.addWidget(self.intervalRadioButton, 7, 0, 1, 3)
        self.layout.addWidget(self.ordinalRadioButton, 8, 0, 1, 3)
        self.layout.addWidget(self.frequencyRadioButton, 9, 0, 1, 3)
        self.layout.addWidget(self.newLine, 10, 0, 1, 3)

        self.layout.addWidget(self.newCSVButton, 11, 0, 1, 3)
        self.layout.addWidget(self.clearButton, 12, 0, 1, 3)
        self.layout.addWidget(self.goButton, 13, 0, 1, 3)
        self.CustomGroup.setFixedWidth(700)
        self.CustomGroup.setLayout(self.layout)

# Changes the QLineEdits to be ReadOnly when
# allRadioButtton is clicked
    def allRadioButtonClicked(self, enabled):
        if enabled:
            self.beginRow.setReadOnly(True)
            self.beginCol.setReadOnly(True)
            self.endRow.setReadOnly(True)
            self.endCol.setReadOnly(True)

# Changes the QLineEdits to not be ReadOnly when
# selectionRadioButtton is clicked
    def selectionRadioButtonClicked(self, enabled):
        if enabled:
            self.beginRow.setReadOnly(False)
            self.beginCol.setReadOnly(False)
            self.endRow.setReadOnly(False)
            self.endCol.setReadOnly(False)

# Populates the table with data from a CSV File
# when newCSVButton is clicked
    def newCSVButtonClicked(self):
        self.openMadeSheet()

    def openMadeSheet(self):
        path = QFileDialog.getOpenFileName(self, "Open CSV", os.getenv("HOME"), "CSV(*.csv)")
        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                self.myTable.setRowCount(0)
                self.myTable.setColumnCount(5)
                my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    row = self.myTable.rowCount()
                    self.myTable.insertRow(row)
                    if len(row_data) > 10:
                        self.myTable.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.myTable.setItem(row, column, item)

        #
# class Table(QTableWidget):
#     def __init__(self, rows, columns):
#         super().__init__(rows, columns)
#         self.checkChange = True
#         self.initUi()
#
#     def initUi(self):
#         self.cellChanged.connect(self.currentCell)
#         self.show()
#
#     def currentCell(self):
#         if self.checkChange:
#             row = self.currentRow()
#             col = self.currentColumn()
#             value = self.item(row, col)
#             value = value.text()
#
#     def openMadeSheet(self):
#         self.checkChange = False
#         path = QFileDialog.getOpenFileName(self, "Open CSV", os.getenv("HOME"), "CSV(*.csv)")
#         if path[0] != '':
#             with open(path[0], newline='') as csv_file:
#                 self.setRowCount(0)
#                 self.setColumnCount(10)
#                 my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
#                 for row_data in my_file:
#                     row = self.rowCount()
#                     self.insertRow(row)
#                     if len(row_data) > 10:
#                         self.setColumnCount(len(row_data))
#                     for column, stuff in enumerate(row_data):
#                         item = QTableWidgetItem(stuff)
#                         self.setItem(row, column, item)
#
#         self.checkChange = True
