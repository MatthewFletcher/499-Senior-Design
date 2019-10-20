from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QRadioButton,QGroupBox,
                             QPushButton, QGridLayout, QSizePolicy, QButtonGroup,
                             QApplication)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pathlib import Path
import sys, os
sys.path.append(str(Path(os.getcwd()).joinpath("../csvtools").resolve()))
import CSV_Wizard
import random
# import UserSelect

class GraphTab(QWidget):
    def __init__(self):
        super().__init__()

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

# The left side of DataTab containing the Table
    def createGraphGroup(self):
        self.GraphGroup = QGroupBox()

        self.figure = plt.figure()
        self.myGraph = FigureCanvas(self.figure)

        self.GraphGroup.setFixedWidth(self.graphWidth)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.myGraph)
        self.GraphGroup.setLayout(self.layout)

# The right side of GraphTab containing Radio Buttons and
# text boxes for user input on how they want their graph
    def createCustomGroup(self):
        self.CustomGroup = QGroupBox()
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # Ask user what they'd like to graph
        self.graphLabel = QLabel("Pick the type of graph you want")
        self.typeGroup = QButtonGroup()
        self.vbarRadioButton = QRadioButton("Vertical bar")
        self.hbarRadioButton = QRadioButton("Horizontal bar")
        self.pieRadioButton = QRadioButton("Pie chart")
        self.lineRadioButton = QRadioButton("Line")
        self.typeGroup.addButton(self.vbarRadioButton)
        self.typeGroup.addButton(self.hbarRadioButton)
        self.typeGroup.addButton(self.pieRadioButton)
        self.typeGroup.addButton(self.lineRadioButton)

        # self.pieRadioButton.setEnabled(False)

        # Buttons to let the user submit the data

        self.graphButton = QPushButton("Graph")
        self.graphButton.setDefault(True)
        self.graphButton.setFixedWidth(680)
        self.graphButton.clicked.connect(self.graphButtonClicked)

        # Button to let the user save the graph as a PNG file
        self.PNGButton = QPushButton("Save as PNG")
        self.PNGButton.setDefault(True)
        self.PNGButton.setFixedWidth(680)
        self.PNGButton.clicked.connect(self.PNGButtonClicked)

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.graphLabel, 1, 0)
        self.layout.addWidget(self.vbarRadioButton, 2, 0)
        self.layout.addWidget(self.hbarRadioButton, 3, 0)
        self.layout.addWidget(self.pieRadioButton, 4, 0)
        self.layout.addWidget(self.lineRadioButton, 5, 0)
        
        self.layout.addWidget(self.graphButton)
        self.CustomGroup.setFixedWidth(700)
        self.CustomGroup.setLayout(self.layout)

        self.layout.addWidget(self.PNGButton)
        self.CustomGroup.setFixedWidth(700)
        self.CustomGroup.setLayout(self.layout)

    # Call this function when the graph button is clicked
    def graphButtonClicked(self):
        masterDF = CSV_Wizard.openFile("../../TestData/IntervalDataTest.csv")
        # contains numpy array
        d = masterDF[0]
        self.figure.clear()
        if self.vbarRadioButton.isChecked() == True:
            self.verticalBarGraph(d)
        elif self.hbarRadioButton.isChecked() == True:
            self.horizontalBarGraph(d)
        elif self.pieRadioButton.isChecked() == True:
            self.ordinal_pie(d)
        elif self.lineRadioButton.isChecked() == True:
            self.lineGraph(d)

        self.myGraph.draw()
        self.repaint()

    def PNGButtonClicked(self):
        self.saveFileDialog()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;PNG Files (*.png)", options=options)
        if fileName:
            self.figure.savefig(fileName)

    # This function will graph the frequency or interval data as a horizontal bar graph
    def horizontalBarGraph(self, df):
        plot = self.figure.add_subplot(111)
        headers = list(df.columns.values)
        headers.pop(0)
        x = headers
        y = []
        for header in headers:
            y.append(df[header].sum())

        plot.barh(x, y)

    def lineGraph(self, df):
        plot = self.figure.add_subplot(111)
        headers = list(df.columns.values)

        x = df[headers[1]]
        y = df[headers[2]]
        plot.set_xlabel(headers[1])
        plot.set_ylabel(headers[2])

        # Plot the points using matplotlib
        plot.plot(x, y)

    # This function will graph frequency or interval data as a vertical bar graph
    def verticalBarGraph(self, df):
        plot = self.figure.add_subplot(111)
        headers = list(df.columns.values)
        headers.pop(0)
        x = headers
        y = []
        for header in headers:
            y.append(df[header].sum())

        plot.bar(x, y)

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
        colors = ['gold', 'yellowgreen']

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


