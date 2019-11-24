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
        self.textWidth = self.size.width() * 0.65
        self.saveWidth = self.size.width() * 0.3

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
        self.infoLabel= QLabel("Analysis Summary \nReport Log")
        self.spaceLabel = QLabel("\n\n\n")

        
        self.SaveTextButton = QPushButton("Save as Text File")
        self.SaveTextButton.setDefault(True)
        #self.SaveButton.setFixedWidth(self.buttonSize)
        self.SaveTextButton.clicked.connect(self.SaveTextClicked)#save as text file
        
        #TODO: CREAte new button to save as csv file
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
        

    def SaveCSVClicked(self):
        self.saveCSVFileDialog()
    def saveCSVFileDialog(self):
        options = QFileDialog.Option()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _= QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "","All Files(*);;Text Files (*.txt)", options=options)
        msg=self.logTextBox.getTexttoFile()
        if fileName:
            print('inside\n')
            test=msg.split('\n')
            with open(fileName, 'w') as csvFile:
                writer=csv.writer(csvFile)
                for text in test:
                    writer.writerow(text)
            csvFile.close()
            

    

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
