from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QRadioButton, QGroupBox,
                             QPushButton, QGridLayout, QSizePolicy, QButtonGroup,
                             QApplication, QFileDialog, QPlainTextEdit, QDialog, QTextEdit, QListView, )
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import sys
import os
import logging
import csv

#logging.info('') e.g. to log 
#note: logs need to happen after everything is initilized.

# The SummaryTab class holds the GUI for the SummaryTab, which consists of two sections:
# the SummaryTextGroup and the SaveTextGroup. The SummaryTextGroup contains the summary
# of what the user has done with the application. The SaveTextGroup contains the button
# that allows the user to save the summary.
class SummaryTab(QWidget):
    def __init__(self):
        super().__init__()

        self.app = QApplication(sys.argv)
        self.screen = self.app.primaryScreen()
        self.size = self.screen.size()

        # These numbers are arbitrary and seemed
        # to have the best balance
        self.buttonSize = 680
        self.textWidth = self.size.width() * 0.64
        self.saveWidth = self.size.width() * 0.29

        self.createSummaryTextGroup()
        self.createSaveTextGroup()

        self.layout = QGridLayout()
        self.layout.addWidget(self.SummaryTextGroup, 0, 0, 0, 1)
        self.layout.addWidget(self.SaveTextGroup, 0, 1)
        
        self.setLayout(self.layout)
        self.show()

    # The left side of SummaryTab containing the logging
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

        self.layout = QGridLayout()
        self.layout.addWidget(self.logTextBox.widget)
        self.SummaryTextGroup.setLayout(self.layout)

    # The right side of AnalysisTab containing the buttons for
    # summaryTab: Clear, Save Text file, Save CSV file
    def createSaveTextGroup(self):

        self.SaveTextGroup = QGroupBox("Options")
        self.SaveTextGroup.setFixedWidth(self.saveWidth)
        self.setStyleSheet("font: 15pt Tw Cen MT")
        self.infoLabel= QLabel("Analysis Summary \nReport Log")
        self.spaceLabel = QLabel("\n\n\n")

        
        self.SaveTextButton = QPushButton("Save as Text File")
        self.SaveTextButton.setDefault(True)
        #self.SaveButton.setFixedWidth(self.buttonSize)
        self.SaveTextButton.clicked.connect(self.SaveTextClicked)#save as text file
        
        #TODO: Create new button to save as csv file
        self.SaveCSVButton = QPushButton("Save as CSV File")
        self.SaveCSVButton.setDefault(True)
        self.SaveCSVButton.clicked.connect(self.SaveCSVClicked)#save as csv file

        self.ClearButtoon = QPushButton("Clear")
        self.ClearButtoon.setDefault(True)
        self.ClearButtoon.clicked.connect(self.ClearButtonClicked)

        self.layout = QGridLayout()
        self.layout.addWidget(self.infoLabel)
        self.layout.addWidget(self.spaceLabel)
        self.layout.addWidget(self.SaveCSVButton)
        self.layout.addWidget(self.SaveTextButton)
        self.layout.addWidget(self.ClearButtoon)
        self.SaveTextGroup.setLayout(self.layout)
        
    #User saves as CSV file
    def SaveCSVClicked(self):
        self.saveCSVFileDialog()
    def saveCSVFileDialog(self):
        options = QFileDialog.Option()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _= QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "","All Files(*);;Text Files (*.txt)", options=options)
        msg=self.logTextBox.getTexttoFile() #retrieve the current list
        if fileName:
            splitMsg=msg.split('\n')#split msg if they are in new row
            with open(fileName, 'w', newline='') as outfile:
                writer=csv.writer(outfile)
                for text in splitMsg:
                    writer.writerow([text])
    

    #User saves as text file
    def SaveTextClicked(self):
        self.saveTextFileDialog()  

    def saveTextFileDialog(self):
        options = QFileDialog.Options()
        options |=  QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()","","All Files(*);;Text Files (*.txt)",options=options)
        msg=self.logTextBox.getTexttoFile()
        if fileName:
            file= open(fileName, "w")
            file.write(msg)
            file.close()

    #User clears the summary in the GUI
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
