from PyQt5.QtWidgets import (QLabel, QGridLayout, QWidget, QMainWindow)
from PyQt5.QtGui import QPixmap


class WelcomeTab(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralWidget = QWidget()
        self.labelText = QLabel(self)
        self.infoText = QLabel(self)
        self.layout = QGridLayout()
        self.pixmap = QPixmap("StatsLogo1.png")
        self.pixmap2 = self.pixmap.scaled(600, 600)
        self.label = QLabel(self)
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 1000
        self.initUi()

    def initUi(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()

        self.show()

    def createGridLayout(self):
        self.label.setPixmap(self.pixmap2)

        #self.labelText.setAlignment(Qt.AlignCenter)
        self.labelText.setStyleSheet("font: 18pt Tw Cen MT")
        self.labelText.setText("Welcome to the Stats Wiz! Here's all you need to know:\n\n"
                               "Data Tab:\nData can be manually entered into a table or uploaded from a CSV File.\n"
                               "The rest of the capabilities will be dependent upon the type of data you entered\n"
                               "(ordinal, interval, or frequency).\n\n"
                               "Graph Tab:\nOur application will graph your data with your choice of "
                               "graph-\nHorizontal bar chart, vertical bar chart, pie chart, normal distribution "
                               "curve, or X-Y graph.\n\n"
                               "Analysis Tab:\nWe can run the following statistical analyses on your data-\nmean, "
                               "median, mode, standard deviation, variance, coefficient of variance,\npercentiles, "
                               "probability distribution, binomial distribution,\nleast square line, X^2 (Chi Square), "
                               "correlation coefficient, sign test,\nrank sum test, and Spearman rank correlation "
                               "coefficient.\n\n"
                               "Summary Tab:\nHere you can see a summary of all you did to your data.\n")

        self.layout.addWidget(self.labelText, 0, 1)
        self.layout.addWidget(self.label, 0, 0)

        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.layout)