from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget
from PyQt5.QtGui import QIcons
import sys 

class TabWdiget(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stats Wiz")
        self.setWindowIcon(QIcon("StatsLogo1.png"))