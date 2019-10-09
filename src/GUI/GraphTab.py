from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTableWidget, QRadioButton,
                             QGroupBox, QPushButton, QGridLayout)

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

        self.myGraph = QTableWidget(400, 400)

        self.GraphGroup.setFixedWidth(1750)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.myGraph)
        self.GraphGroup.setLayout(self.layout)

# The right side of DataTab containing Radio Buttons and
# text boxes for user input on how they want their graph
    def createCustomGroup(self):
        self.CustomGroup = QGroupBox()
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # Ask user what they'd like to graph
        self.graphLabel = QLabel("Pick the type of graph you want")
        self.graphLabelhi = QLabel("hi")
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
        self.layout.addWidget(self.graphLabel, 1, 0)
        self.layout.addWidget(self.vbarRadioButton, 2, 0)
        self.layout.addWidget(self.hbarRadioButton, 3, 0)
        self.layout.addWidget(self.pieRadioButton, 4, 0)
        self.layout.addWidget(self.lineRadioButton, 5, 0)

        self.layout.addWidget(self.newPNGButton)
        self.CustomGroup.setFixedWidth(700)
        self.CustomGroup.setLayout(self.layout)

