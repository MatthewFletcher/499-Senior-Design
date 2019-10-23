from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QGroupBox)
import sys


class AnalysisTab(QWidget):
    def __init__(self):
        super().__init__()

        self.app = QApplication(sys.argv)
        self.screen = self.app.primaryScreen()
        self.size = self.screen.size()

        self.tableWidth = self.size.width() * 0.65
        self.customWidth = self.size.width() * 0.3

        self.show()

        # The right side of DataTab containing Radio Buttons and
        # text boxes for user input on how they want their graph
        def createCustomGroup(self):
            self.CustomGroup = QGroupBox()
            self.setStyleSheet("font: 15pt Tw Cen MT")
