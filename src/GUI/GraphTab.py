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
        self.vbarRadioButton = QRadioButton("Vertical bar")
        self.hbarRadioButton = QRadioButton("Horizontal bar")
        self.pieRadioButton = QRadioButton("Pie chart")
        self.lineRadioButton = QRadioButton("Line")


        # Buttons to let the user submit the data
        self.newPNGButton = QPushButton("Save PNG")
        self.newPNGButton.setDefault(True)
        self.newPNGButton.setFixedWidth(680)

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.graphLabel)
        self.layout.addWidget(self.vbarRadioButton)
        self.layout.addWidget(self.hbarRadioButton)
        self.layout.addWidget(self.pieRadioButton)
        self.layout.addWidget(self.lineRadioButton)

        self.layout.addWidget(self.newPNGButton)
        self.CustomGroup.setFixedWidth(700)
        self.CustomGroup.setLayout(self.layout)

