from PyQt5.QtWidgets import (QApplication, QTabWidget, QDialog,
QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
QTextEdit, QLineEdit, QMainWindow, QFileDialog)
from PyQt5.QtGui import QIcon
import os
import csv
import sys 

class SummaryTab(QWidget):
    def __init__(self):
        super().__init__()