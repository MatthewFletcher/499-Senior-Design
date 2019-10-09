from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
                             QLineEdit, QFileDialog, QRadioButton, QGroupBox, QPushButton,
                             QGridLayout, QButtonGroup)
from PyQt5.QtGui import QIcon
import os
import csv
import sys
import PyQt5

class GraphTab(QWidget):
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
        self.graphLabel = QLabel("Pick the type of graph you want")
        self.graphGroup = QButtonGroup()
        self.vbarRadioButton = QRadioButton("Vertical bar")
        self.hbarRadioButton = QRadioButton("Horizontal bar")
        self.pieRadioButton = QRadioButton("Pie chart")
        self.lineRadioButton = QRadioButton("Line")
        self.graphGroup.addButton(self.vbarRadioButton)
        self.graphGroup.addButton(self.hbarRadioButton)
        self.graphGroup.addButton(self.pieRadioButton)
        self.graphGroup.addButton(self.lineRadioButton)
        self.vbarRadioButton.toggled.connect(self.vbarRadioButtonClicked)
        self.hbarRadioButton.toggled.connect(self.hbarRadioButtonClicked)
        self.pieRadioButton.toggled.connect(self.pieRadioButtonClicked)
        self.lineRadioButton.toggled.connect(self.lineRadioButtonClicked)

        # Buttons to let the user submit the data
        self.newPNGButton = QPushButton("Save PNG")
        self.newPNGButton.setDefault(True)
        self.newPNGButton.setFixedWidth(680)
        self.newPNGButton.clicked.connect(self.newPNGButtonClicked)

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.graphLabel, 0, 0, 1, 4)
        self.layout.addWidget(self.vbarRadioButton, 1, 0, 1, 3)
        self.layout.addWidget(self.hbarRadioButton, 2, 0, 1, 3)
        self.layout.addWidget(self.pieRadioButton, 3, 0, 1, 3)
        self.layout.addWidget(self.lineRadioButton, 4, 0, 1, 3)

        self.layout.addWidget(self.newPNGButton, 11, 0, 1, 3)
        self.CustomGroup.setFixedWidth(700)
        self.CustomGroup.setLayout(self.layout)

    def vbarRadioButtonClicked(self, enabled):
        if enabled:
            self.beginRow.setReadOnly(True)
            self.beginCol.setReadOnly(True)
            self.endRow.setReadOnly(True)
            self.endCol.setReadOnly(True)

    def hbarRadioButtonClicked(self, enabled):
        if enabled:
            self.beginRow.setReadOnly(False)
            self.beginCol.setReadOnly(False)
            self.endRow.setReadOnly(False)
            self.endCol.setReadOnly(False)

    def pieRadioButtonClicked(self, enabled):
        if enabled:
            self.beginRow.setReadOnly(True)
            self.beginCol.setReadOnly(True)
            self.endRow.setReadOnly(True)
            self.endCol.setReadOnly(True)

    def lineRadioButtonClicked(self, enabled):
        if enabled:
            self.beginRow.setReadOnly(True)
            self.beginCol.setReadOnly(True)
            self.endRow.setReadOnly(True)
            self.endCol.setReadOnly(True)

# Calls openCSV() function when the
# newCSVButton is clicked
    def newPNGButtonClicked(self):
        self.savePNG()

    def savePNG(self):
        path = QFileDialog.getOpenFileName(self, "Open CSV", os.getenv("HOME"), "CSV(*.csv)")
        if path[0] != '':
            with open(path[0], newline='') as csvFile:
                self.myTable.setRowCount(0)
                self.myTable.setColumnCount(5)
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

        self.myTable.setRowCount(400)
        self.myTable.setColumnCount(400)

