from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
                             QLineEdit, QFileDialog, QRadioButton, QGroupBox, QPushButton,
                             QGridLayout, QButtonGroup, QApplication)
import os
import sys
import csv


# The DataTab class holds all the GUI for the DataTab
class DataTab(QWidget):
    def __init__(self):
        super().__init__()

        self.app = QApplication(sys.argv)
        self.screen = self.app.primaryScreen()
        self.size = self.screen.size()

        self.tableWidth = self.size.width() * 0.65
        self.customWidth = self.size.width() * 0.3

        self.buttonSize = self.size.width() * 0.29
        self.lineEditSize = self.size.width() * 0.067
        self.rowSize = 400
        self.columnSize = 400

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

        self.myTable = QTableWidget(self.rowSize, self.columnSize)

        self.TableGroup.setFixedWidth(self.tableWidth)
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
        self.beginRow.setFixedWidth(self.lineEditSize)
        self.beginCol.setFixedWidth(self.lineEditSize)
        self.endRow.setFixedWidth(self.lineEditSize)
        self.endCol.setFixedWidth(self.lineEditSize)

        # Have the QLineEdits only be editable if
        # selectionRadioButton is selected
        self.beginRow.setEnabled(False)
        self.beginCol.setEnabled(False)
        self.endRow.setEnabled(False)
        self.endCol.setEnabled(False)

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
        self.newCSVButton.setFixedWidth(self.buttonSize)
        self.newCSVButton.clicked.connect(self.newCSVButtonClicked)

        self.clearButton = QPushButton("Clear Table")
        self.clearButton.setDefault(True)
        self.clearButton.setFixedWidth(self.buttonSize)
        self.clearButton.clicked.connect(self.clearButtonClicked)

        self.goButton = QPushButton("Submit Data")
        self.goButton.setDefault(True)
        self.goButton.setFixedWidth(self.buttonSize)

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.graphLabel, 0, 0, 1, 3)
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
        self.CustomGroup.setFixedWidth(self.customWidth)
        self.CustomGroup.setLayout(self.layout)

# Changes the QLineEdits to be ReadOnly when
# allRadioButtton is clicked
    def allRadioButtonClicked(self, enabled):
        if enabled:
            self.beginRow.setEnabled(False)
            self.beginCol.setEnabled(False)
            self.endRow.setEnabled(False)
            self.endCol.setEnabled(False)

# Changes the QLineEdits to not be ReadOnly when
# selectionRadioButtton is clicked
    def selectionRadioButtonClicked(self, enabled):
        if enabled:
            self.beginRow.setEnabled(True)
            self.beginCol.setEnabled(True)
            self.endRow.setEnabled(True)
            self.endCol.setEnabled(True)

# Calls openCSV() function when the
# newCSVButton is clicked
    def newCSVButtonClicked(self):
        self.openCSV()

    def clearButtonClicked(self):
        self.clearTable()

# Populates the table with data from a CSV File
# when newCSVButton is clicked
    def openCSV(self):
        path = QFileDialog.getOpenFileName(self, "Open CSV", os.getenv("HOME"), "CSV(*.csv)")
        if path[0] != '':
            with open(path[0], newline='') as csvFile:
                self.myTable.setRowCount(0)
                self.myTable.setColumnCount(self.columnSize)
                myFile = csv.reader(csvFile, delimiter=',', quotechar='|')
                for row_data in myFile:
                    row = self.myTable.rowCount()
                    self.myTable.insertRow(row)
                    if len(row_data) > 10:
                        self.myTable.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.myTable.setItem(row, column, item)

# Clears the table and restores it to the original
    def clearTable(self):
        while self.myTable.rowCount() > 0:
            self.myTable.removeRow(0)

        self.myTable.setRowCount(self.rowSize)
        self.myTable.setColumnCount(self.columnSize)
