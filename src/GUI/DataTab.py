from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
                             QLineEdit, QFileDialog, QRadioButton, QGroupBox, QPushButton,
                             QGridLayout, QButtonGroup, QApplication, QAbstractItemView,
                             QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import os
import sys
import csv
import pandas as pd
import UserSelect
from pathlib import Path
import logging
import AnalysisTab


# The DataTab class holds the GUI for the DataTab, which consists of two sections:
# the TableGroup and the CustomGroup. The TableGroup deals with the table, which
# contains the user's data. The CustomGroup has the user select different
# options based on their data and what they would like graphed.
class DataTab(QWidget):
    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)
        self.screen = self.app.primaryScreen()
        self.size = self.screen.size()
        self.masterDF = None
        self.dataType = None

        self.analysisTab = AnalysisTab

        # These numbers are arbitrary and seemed
        # to have the best balance
        self.tableWidth = self.size.width() * 0.64
        self.customWidth = self.size.width() * 0.29
        self.buttonSize = self.size.width() * 0.28
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
        self.TableGroup = QGroupBox("Table")
        self.myTable = QTableWidget(self.rowSize, self.columnSize)
        self.myTable.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.TableGroup.setFixedWidth(self.tableWidth)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.myTable)
        self.TableGroup.setLayout(self.layout)
        # self.myTable.clicked.connect(self.selectionChanged)

    # The right side of DataTab containing Radio Buttons and
    # text boxes for user input on how they want their graph
    def createCustomGroup(self):
        self.CustomGroup = QGroupBox("Options")
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # Ask user what they'd like to graph
        self.graphLabel = QLabel("How much do you want graphed?")
        self.graphGroup = QButtonGroup()
        self.allRadioButton = QRadioButton("Graph everything")
        self.allRadioButton.setChecked(True)
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
        self.intervalRadioButton.setChecked(True)
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

        self.submitButton = QPushButton("Submit Data")
        self.submitButton.setDefault(True)
        self.submitButton.setFixedWidth(self.buttonSize)

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
        self.layout.addWidget(self.submitButton, 13, 0, 1, 3)
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
    # selectionRadioButton is clicked
    def selectionRadioButtonClicked(self, enabled):
        if enabled:
            self.beginRow.setEnabled(True)
            self.beginCol.setEnabled(True)
            self.endRow.setEnabled(True)
            self.endCol.setEnabled(True)

    # Calls openCSV() function when the
    # newCSVButton is clicked
    def newCSVButtonClicked(self):
        logging.info('Import CSV Button Selected')
        self.openCSV()

    def clearButtonClicked(self):
        logging.info('Clear Data Button Selected')
        self.clearTable()

    # Populates the table with data from a CSV File
    # when newCSVButton is clicked
    def openCSV(self):
        path = QFileDialog.getOpenFileName(self, "Open CSV", os.getenv("HOME"), "CSV(*.csv)")
        if path[0] != '':
            logging.info("Opening the CSV file")
            with open(path[0], newline='') as csvFile:
                myFile = csv.reader(csvFile, delimiter=',', quotechar='|')
                headers = next(myFile)
                self.myTable.setRowCount(0)
                self.myTable.setColumnCount(len(headers))
                self.myTable.setHorizontalHeaderLabels(headers)
                for row_data in myFile:
                    row = self.myTable.rowCount()
                    self.myTable.insertRow(row)
                    if len(row_data) > 10:
                        self.myTable.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem()
                        item.setData(Qt.EditRole, stuff)
                        self.myTable.setItem(row, column, item)

    #  This function will be able to grab the data imported from the table
    # and store it as a df to be used for graphing the data
    def getDataFromTable(self):
        # Condition statement to determine if the table is empty,
        # send error message
        if self.myTable.item(0,0) is None:
            self.errorMessage()
        else:
            # Get data from table and store as df
            number_of_rows = self.myTable.rowCount()
            number_of_columns = self.myTable.columnCount()
            if number_of_columns == 1:
                self.analysisTab.enableAnalysisStatistics(self.dataTab.getDataType())
            header = []
            for i in range(number_of_columns):
                header.append(self.myTable.horizontalHeaderItem(i).text())
            tmp_df = pd.DataFrame(columns=header, index=range(number_of_rows))

            for i in range(number_of_rows):
                tmp_df.iloc[i, 0] = self.myTable.item(i, 0).text()
                for j in range(1, number_of_columns):
                    tmp_df.iloc[i, j] = int(self.myTable.item(i, j).text())
            if self.allRadioButton.isChecked():
                logging.info('User Selection on Dataset')
                ptA = [0, 1]
                ptB = [number_of_rows - 1, number_of_columns - 1]
                self.sentSuccess()
                return UserSelect.selection(tmp_df, ptA, ptB, 1)
            else:
                # This is when the user clicks "Let me pick what to graph"
                # Condition to determine if any of column or row bounds
                # are left empty by the user, send error message
                if self.beginRow.text() == "" or self.beginCol.text() == "" or self.endCol.text() == "" or self.endRow.text() == "":
                    self.errorMissingRange()
                else:
                    x1 = int(self.beginRow.text()) - 1
                    y1 = int(self.beginCol.text())
                    x2 = int(self.endRow.text()) - 1
                    y2 = int(self.endCol.text())
                    # If any of the column or row bounds specified by the user
                    # are out of bounds, send error message
                    if x1 < 0 or x1 > number_of_rows or x2 < 0 or x2 > number_of_rows or x2 < x1 or y1 < 1 or y1 > number_of_columns or y2 < 1 or y2 > number_of_columns or y2 < y1:
                        self.errorOutofBounds()
                    else:
                        ptA = [x1, y1]
                        ptB = [x2, y2]
                        print (UserSelect.selection(tmp_df, ptA, ptB, 1))
                        self.sentSuccess()
                        return UserSelect.selection(tmp_df, ptA, ptB, 1)

    def getDataType(self):
        if self.intervalRadioButton.isChecked():
            return "interval"
        elif self.ordinalRadioButton.isChecked():
            return "ordinal"
        elif self.frequencyRadioButton.isChecked():
            return "frequency"

    # Clears the table and restores it to the original
    def clearTable(self):
        logging.info('clearing the dataset table')
        while self.myTable.rowCount() > 0:
            self.myTable.removeRow(0)

        for i in range(0, self.rowSize):
            self.myTable.setHorizontalHeaderItem(i, QTableWidgetItem("{0}".format(i + 1)))

        self.myTable.setRowCount(self.rowSize)
        self.myTable.setColumnCount(self.columnSize)

    def errorMessage(self):
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setWindowIcon(QIcon("StatsLogo1.png"))
        error.setText("You haven't entered any information in the table!")
        error.setStandardButtons(QMessageBox.Ok)
        error.exec()

    def errorMissingRange(self):
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setWindowIcon(QIcon("StatsLogo1.png"))
        error.setText("You need to specify all of the range of values!")
        error.setStandardButtons(QMessageBox.Ok)
        error.exec()

    def errorOutofBounds(self):
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setWindowIcon(QIcon("StatsLogo1.png"))
        error.setText("Your column or row index is out of bounds!\n")
        error.setStandardButtons(QMessageBox.Ok)
        error.exec()

    def sentSuccess(self):
        success = QMessageBox()
        success.setWindowTitle("Success")
        success.setWindowIcon(QIcon("StatsLogo1.png"))
        success.setText("Your data was sent!\n")
        success.setStandardButtons(QMessageBox.Ok)
        success.exec()