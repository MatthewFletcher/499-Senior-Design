from PyQt5.QtWidgets import (QApplication, QTabWidget, QDialog,
QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
QTextEdit, QLineEdit, QMainWindow, QFileDialog)
from PyQt5.QtGui import QIcon
import os
import csv
import sys 

class TabWdiget(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stats Wiz")
        self.setWindowIcon(QIcon("StatsLogo1.png"))
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 1000

        tabwidget = QTabWidget()
        tabwidget.addTab(DataTab(), "Data Input")
        tabwidget.addTab(GraphTab(), "Graph")
        tabwidget.addTab(AnalysisTab(), "Analysis")
        tabwidget.addTab(SummaryTab(), "Summary")

        vbox = QVBoxLayout()
        vbox.addWidget(tabwidget)

        self.setLayout(vbox)



class DataTab(QWidget):
    def __init__(self):
        super().__init__()

        self.form_widget = Table(10, 10)

        self.form_widget.openSheet()
        self.show()




class GraphTab(QWidget):
    def __init__(self):
        super().__init__()



class AnalysisTab(QWidget):
    def __init__(self):
        super().__init__()



class SummaryTab(QWidget):
    def __init__(self):
        super().__init__()



class Table(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.checkChange = True
        self.initUi()

    def initUi(self):
        self.cellChanged.connect(self.currentCell)
        self.show()

    def currentCell(self):
        if self.checkChange:
            row = self.currentRow()
            col = self.currentColumn()
            value = self.item(row, col)
            value = value.text()

    def openSheet(self):
        self.checkChange = False
        path = QFileDialog.getOpenFileName(self, "Open CSV", os.getenv("HOME"), "CSV(*.csv)")
        if path[0] != '':
            with open(path[0], newline = '') as csv_file:
                self.setRowCount(0)
                self.setColumnCount(10)
                my_file = csv.reader(csv_file, delimiter = ',' | '  ', quotechar = '|')
                for row_data in my_file:
                    row = self.rowCount()
                    self.insertRow(row)
                    if len(row_data) > 10:
                        self.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)

        self.checkChange = True


app = QApplication(sys.argv)
tabwidget = TabWdiget()
tabwidget.show()
app.exec()