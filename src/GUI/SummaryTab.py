from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout, QPushButton, QGroupBox)
import sys


class SummaryTab(QWidget):
    def __init__(self):
        super().__init__()

        self.app = QApplication(sys.argv)
        self.screen = self.app.primaryScreen()
        self.size = self.screen.size()

        self.textWidth = self.size.width() * 0.75
        self.saveWidth = self.size.width() * 0.2

        self.createSummaryTextGroup()
        self.createSaveTextGroup()

        self.layout = QGridLayout()
        self.layout.addWidget(self.SummaryTextGroup, 0, 0, 0, 1)
        self.layout.addWidget(self.SaveTextGroup, 0, 1)
        self.setLayout(self.layout)
        self.show()

    # The left side of AnalysisTab containing the textbox
    # where the analysis will be shown
    def createSummaryTextGroup(self):
        self.SummaryTextGroup = QGroupBox("Summary")
        self.SummaryTextGroup.setFixedWidth(self.textWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # Here is where the analysis will go
        self.analysis = QLabel()

        self.layout = QGridLayout()
        self.layout.addWidget(self.analysis)
        self.SummaryTextGroup.setLayout(self.layout)

    # The right side of AnalysisTab containing the buttons for
    # analysis
    def createSaveTextGroup(self):
        self.SaveTextGroup = QGroupBox("Save Analysis")
        self.SaveTextGroup.setFixedWidth(self.saveWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")

        self.spaceLabel = QLabel("\n\n\n\n")

        self.SaveButton = QPushButton("Download")

        self.layout = QGridLayout()
        self.layout.addWidget(self.spaceLabel)
        self.layout.addWidget(self.SaveButton)
        self.SaveTextGroup.setLayout(self.layout)
