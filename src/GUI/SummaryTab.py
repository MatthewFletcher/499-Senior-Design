#from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout,
#                             QPushButton, QGroupBox, QPlainTextEdit)
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QRadioButton, QGroupBox,
                             QPushButton, QGridLayout, QSizePolicy, QButtonGroup,
                             QApplication, QFileDialog, QPlainTextEdit, QDialog, QTextEdit, QListView, )
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import sys
import os
import logging
#logging.info('') e.g. to log 
#note: logs need to happen after everything is initilized.

class SummaryTab(QWidget):
    def __init__(self):
        super().__init__()
       
        self.app = QApplication(sys.argv)
        self.screen = self.app.primaryScreen()
        self.size = self.screen.size()

        self.buttonSize = 680
        self.textWidth = self.size.width() * 0.75
        self.saveWidth = self.size.width() * 0.2

        self.createSummaryTextGroup()
        self.createSaveTextGroup()
        

        self.layout = QGridLayout()
        self.layout.addWidget(self.SummaryTextGroup, 0, 0, 0, 1)
        self.layout.addWidget(self.SaveTextGroup, 0, 1)
        
        
        self.setLayout(self.layout)
        self.show()


    # The left side of SummaryTab containing the textbox
    # where the summary will be shown
    def createSummaryTextGroup(self):
        self.SummaryTextGroup = QGroupBox("Summary")
        self.SummaryTextGroup.setFixedWidth(self.textWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")

        # Here is where the summary will go
        self.analysis = QLabel(self)
        
        #Create Handler to display text in gui
        self.logTextBox=QPlainTextEditLogger(self.analysis)
        self.logTextBox.setFormatter(logging.Formatter("%(levelname)s %(filename)s -%(message)s"))
        logging.getLogger().addHandler(self.logTextBox)
        logging.getLogger().setLevel(logging.INFO) #just need analysis results not too much detailed.
        logging.getLogger().propagate=False
        
        
        #Example of logging text.
        #TODO: Remove log test loop
        for x in range(60):
            logging.info('testing: display text %d',x)

            
        self.layout = QGridLayout()
        self.layout.addWidget(self.analysis)
        self.layout.addWidget(self.logTextBox.widget)
        self.SummaryTextGroup.setLayout(self.layout)

    # The right side of AnalysisTab containing the buttons for
    # summaryTab
    def createSaveTextGroup(self):
        self.SaveTextGroup = QGroupBox("Options")
        self.SaveTextGroup.setFixedWidth(self.saveWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")
        self.infoLabel= QLabel("Analysis Summary Report Log")
        self.spaceLabel = QLabel("\n\n\n")

        self.SaveButton = QPushButton("Save")
        self.SaveButton.setDefault(True)
        #self.SaveButton.setFixedWidth(self.buttonSize)
        self.SaveButton.clicked.connect(self.SaveButtonClicked)

        self.ClearButtoon = QPushButton("Clear")
        self.ClearButtoon.setDefault(True)
        self.ClearButtoon.clicked.connect(self.ClearButtonClicked)

        self.layout = QGridLayout()
        self.layout.addWidget(self.infoLabel)
        self.layout.addWidget(self.spaceLabel)
        self.layout.addWidget(self.SaveButton)
        self.layout.addWidget(self.ClearButtoon)
        self.SaveTextGroup.setLayout(self.layout)
        
    def SaveButtonClicked(self):
        self.saveFileDialog()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |=  QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()","","All Files(*);;Text Files (*.txt)",options=options)
        msg=self.logTextBox.getTexttoFile()
        if fileName:
            file= open(fileName, "w")
            file.write(msg)
            file.close()
    def ClearButtonClicked(self):
        self.logTextBox.deleteTextinGUI()

    

class QPlainTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.messages=''
        self.widget=QPlainTextEdit(parent)
        self.widget.setReadOnly(True)
    def emit(self, record):
        msg=self.format(record)
        self.messages+=msg
        self.widget.appendPlainText(msg)
    def getTexttoFile(self):
        return self.widget.toPlainText()
    def deleteTextinGUI(self):
        self.widget.clear()


    
"""
class TextLogger(logging.Handler):
    def __init__(self):
        super().__init__()

        self.log = QPlainTextEdit()
        self.log.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.textCursor().appendPlainText(msg)

    def write(self, m):
        pass
#"""

