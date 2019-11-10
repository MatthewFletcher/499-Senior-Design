from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QRadioButton, QGroupBox,
                             QPushButton, QGridLayout, QSizePolicy, QButtonGroup,
                             QApplication, QFileDialog)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import sys, os

import logging

class GraphTab(QWidget):
    def __init__(self):
        super().__init__()
        self.masterDF = None
        self.app = QApplication(sys.argv)
        self.screen = self.app.primaryScreen()
        self.size = self.screen.size()

        self.buttonSize = 680
        self.graphWidth = self.size.width() * 0.65
        self.customWidth = self.size.width() * 0.3

        self.createGraphGroup()
        self.createCustomGroup()

        self.layout = QGridLayout()
        self.layout.addWidget(self.GraphGroup, 0, 0, 0, 1)
        self.layout.addWidget(self.CustomGroup, 0, 1)
        self.setLayout(self.layout)
        self.show()

    # The left side of GraphTab containing the Graph
    def createGraphGroup(self):
        self.GraphGroup = QGroupBox("Graph")

        self.figure = plt.figure()
        self.myGraph = FigureCanvas(self.figure)

        self.GraphGroup.setFixedWidth(self.graphWidth)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.myGraph)
        self.GraphGroup.setLayout(self.layout)

    # The right side of GraphTab containing Radio Buttons and
    # text boxes for user input on how they want their graph
    def createCustomGroup(self):
        self.CustomGroup = QGroupBox("Options")
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # Ask user what they'd like to graph
        self.graphLabel = QLabel("What kind of graph would you like?")
        self.typeGroup = QButtonGroup()
        self.vbarRadioButton = QRadioButton("Vertical bar")
        self.hbarRadioButton = QRadioButton("Horizontal bar")
        self.pieRadioButton = QRadioButton("Pie chart")
        self.NDCRadioButton = QRadioButton("Normal Distribution Curve")
        self.scatterRadioButton = QRadioButton("Scatter plot")
        self.typeGroup.addButton(self.vbarRadioButton)
        self.typeGroup.addButton(self.hbarRadioButton)
        self.typeGroup.addButton(self.pieRadioButton)
        self.typeGroup.addButton(self.NDCRadioButton)
        self.typeGroup.addButton(self.scatterRadioButton)
        self.spaceLabel = QLabel("\n\n\n")

        # Buttons to let the user submit the data
        self.graphButton = QPushButton("Graph")
        self.graphButton.setDefault(True)
        self.graphButton.setFixedWidth(self.buttonSize)
        self.graphButton.clicked.connect(self.graphButtonClicked)

        # Button to let the user save the graph as a PNG file
        self.PNGButton = QPushButton("Save as PNG")
        self.PNGButton.setDefault(True)
        self.PNGButton.setFixedWidth(self.buttonSize)
        self.PNGButton.clicked.connect(self.PNGButtonClicked)

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.graphLabel, 1, 0)
        self.layout.addWidget(self.vbarRadioButton, 2, 0)
        self.layout.addWidget(self.hbarRadioButton, 3, 0)
        self.layout.addWidget(self.pieRadioButton, 4, 0)
        self.layout.addWidget(self.NDCRadioButton, 5, 0)
        self.layout.addWidget(self.scatterRadioButton, 6, 0)
        self.layout.addWidget(self.spaceLabel, 7, 0)

        self.layout.addWidget(self.graphButton)
        self.CustomGroup.setFixedWidth(self.buttonSize)
        self.CustomGroup.setLayout(self.layout)

        self.layout.addWidget(self.PNGButton)
        self.CustomGroup.setFixedWidth(self.buttonSize)
        self.CustomGroup.setLayout(self.layout)

    def enableGraphType(self, dataType):
        if dataType == "interval" or dataType == "frequency":
            self.vbarRadioButton.setEnabled(True)
            self.hbarRadioButton.setEnabled(True)
            self.NDCRadioButton.setEnabled(True)
            self.pieRadioButton.setEnabled(True)
        elif dataType == "ordinal":
            self.vbarRadioButton.setEnabled(True)
            self.hbarRadioButton.setEnabled(True)
            self.NDCRadioButton.setEnabled(True)
            self.pieRadioButton.setEnabled(True)
            self.scatterRadioButton.setEnabled(False)

    # Call this function when the graph button is clicked
    def graphButtonClicked(self):
        logging.info('Graphing has been selected')
        d = self.masterDF
        self.figure.clear()
        if self.vbarRadioButton.isChecked():
            self.verticalBarGraph(d)
        elif self.hbarRadioButton.isChecked():
            self.horizontalBarGraph(d)
        elif self.pieRadioButton.isChecked():
            self.ordinal_pie(d)
        elif self.lineRadioButton.isChecked():
            self.lineGraph(d)
        elif self.scatterRadioButton.isChecked():
        # elif self.NDCRadioButton.isChecked() == True:
        #     self.NDCGraph(d)

            self.scatterPlot(d)
        logging.info('GraphTab: Data has been graphed')

        self.myGraph.draw()
        self.repaint()

    def PNGButtonClicked(self):
        logging.info('Saving graph as PNG')
        self.saveFileDialog()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "All Files (*);;PNG Files (*.png)", options=options)
        if fileName:
            self.figure.savefig(fileName)

    # This function will graph the data as a horizontal bar graph
    def horizontalBarGraph(self, df):
        plot = self.figure.add_subplot(111)
        headers = list(df.columns.values)
        headers.pop(0)
        x = headers
        y = []
        for header in headers:
            y.append(df[header].sum())

        plot.barh(x, y, color=['orange', 'darkkhaki'])

    # # This function will graph the data as a normal distribution curve
    # def NDCGraph(self, df):


    # def lineGraph(self, df):
    #     plot = self.figure.add_subplot(111)
    #     headers = list(df.columns.values)
    #
    #     x = df[headers[1]]
    #     y = df[headers[2]]
    #     plot.set_xlabel(headers[1])
    #     plot.set_ylabel(headers[2])
    #
    #     # Plot the points using matplotlib
    #     plot.plot(x, y)

    # This function will graph the data as a vertical bar graph
    def verticalBarGraph(self, df):
        plot = self.figure.add_subplot(111)
        headers = list(df.columns.values)
        headers.pop(0)
        x = headers
        y = []
        for header in headers:
            y.append(df[header].sum())

        plot.bar(x, y, color=['lightcoral', 'steelblue'])

    # This function will graph the frequency or interval data as a pie chart
    def freqint_pie(self, df):
        plot = self.figure.add_subplot(111)
        headers = list(df.columns.values)
        # Remove the Question # column
        headers.pop(0)
        x = headers
        y = []
        explode = []
        for header in headers:
            y.append(df[header].sum())
            explode.append(0)

        # Data to plot
        colors = ['gold', 'navyblue']

        # Plot
        plot.pie(y, explode=explode, labels=x, colors=colors,
                 autopct='%1.1f%%', shadow=False, startangle=0)
        plot.axis('equal')

    # This function will graph ordinal data as a pie chart
    def ordinal_pie(self, df):
        plot = self.figure.add_subplot(111)
        headers = list(df.columns.values)
        # Remove the Question # column
        headers.pop(0)
        x = headers
        y = []
        explode = []
        for header in headers:
            y.append(df[header].sum())
            explode.append(0)

        # Data to plot
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lavender']

        # Plot
        plot.pie(y, explode=explode, labels=x, colors=colors,
                 autopct='%1.1f%%', shadow=False, startangle=0)
        plot.axis('equal')

    # This function will graph the data as a scatter plot
    def scatterPlot(self, df):
        plot = self.figure.add_subplot(111)
        headers = list(df.columns.values)

        x = df[headers[1]]
        y = df[headers[2]]
        plot.set_xlabel(headers[1])
        plot.set_ylabel(headers[2])
        plot.scatter(x, y)
