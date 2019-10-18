from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QRadioButton,
                             QGroupBox, QPushButton, QGridLayout, QSizePolicy, QButtonGroup)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from pathlib import Path
import sys, os
sys.path.append(str(Path(os.getcwd()).joinpath("../csvtools").resolve()))
import CSV_Wizard
import UserSelect

class GraphTab(QWidget):
    def __init__(self):
        super().__init__()

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

        self.myGraph = PlotCanvas(self, width=5, height=4)

        self.GraphGroup.setFixedWidth(1750)
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

        #self.typeGroup.clicked.connect(self.process())

        # Buttons to let the user submit the data
        # self.graphButton = QPushButton("Graph")
        # self.graphButton.setDefault(True)
        # self.graphButton.setFixedWidth(680)
        # self.graphButton.clicked.connect(self.graphButtonClicked)

        # Button to let the user save the graph as a PNG file
        # self.PNGButton = QPushButton("Save as PNG")
        # self.PNGButton.setDefault(True)
        # self.PNGButton.setFixedWidth(680)
        # self.PNGButton.clicked.connect(self.PNGButtonClicked)

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.graphLabel, 1, 0)
        self.layout.addWidget(self.vbarRadioButton, 2, 0)
        self.layout.addWidget(self.hbarRadioButton, 3, 0)
        self.layout.addWidget(self.pieRadioButton, 4, 0)
        self.layout.addWidget(self.lineRadioButton, 5, 0)

    #     self.layout.addWidget(self.graphButton)
    #     self.CustomGroup.setFixedWidth(700)
    #     self.CustomGroup.setLayout(self.layout)
    #
    #     self.layout.addWidget(self.PNGButton)
    #     self.CustomGroup.setFixedWidth(700)
    #     self.CustomGroup.setLayout(self.layout)
    #
    # # Call this function when the graph button is clicked
    # def graphButtonClicked(self):
    #
    # def PNGButtonClicked(self):
    #     self.savePNG()
    #
    # # Populates the table with data from a CSV File
    # # when newCSVButton is clicked
    # def savePNG(self):
    #     self.savefig('graph.png')

    def process(self):
        if self.vbarRadioButton.isChecked() == True:
            graph = PlotCanvas.verticalBarGraph()
        elif self.hbarRadioButton.isChecked() == True:
            graph2 = PlotCanvas.horizontalBarGraph()
        elif self.pieRadioButton.isChecked() == True:
            graph3 = PlotCanvas.ordinal_pie()
        elif self.lineRadioButton.isChecked() == True:
            graph4 = PlotCanvas.lineGraph()

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        myinfo = CSV_Wizard.openFile("../../TestData/IntervalDataTest.csv")
        # contains numpy array
        d = myinfo[0]
        self.horizontalBarGraph(d)

    def lineGraph(self, df):
        plot = self.figure.add_subplot(111)
        headers = list(df.columns.values)

        x = df[headers[1]]
        y = df[headers[2]]
        plot.set_xlabel(headers[1])
        plot.set_ylabel(headers[2])

        # Plot the points using matplotlib
        plot.plot(x, y)
        self.draw()

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
        self.draw()

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
        self.draw()

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
        self.draw()

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
        self.draw()

