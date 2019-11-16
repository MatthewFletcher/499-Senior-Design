#"""
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QRadioButton, QGroupBox,
                             QPushButton, QGridLayout, QSizePolicy, QButtonGroup,
                             QApplication, QFileDialog, QPlainTextEdit, QDialog, QTextEdit, QListView, QLabel ,QTreeWidget,QTreeWidgetItem,QVBoxLayout,
                             QHBoxLayout,QFrame, )
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtGui import QPixmap

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import Qt
import sys
import os
from pathlib import Path


class WelcomeTab(QWidget):
    def __init__(self):
        super().__init__()
        #QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        #test on mac
        self.app =QApplication(sys.argv)
        self.screen = self.app.primaryScreen()
        self.size=self.screen.size()
        self.buttonSize=680

        self.logoWidth=self.size.width() *0.33
        self.infoWidth=self.size.width()*0.60
        
        self.createLogoGroup()
        self.createInfoGroup()

        self.layout=QGridLayout()
        self.layout.addWidget(self.logoGroup, 0,0,0,1 )
        self.layout.addWidget(self.infoGroup, 0, 1)

        self.setLayout(self.layout)
        self.show()

        
    #Left side for the picture
    def createLogoGroup(self):
        self.logoGroup =QGroupBox("")
        self.logoGroup.setFixedWidth(self.logoWidth)
        print(self.infoWidth)
        self.pixmap=QPixmap(os.path.join(Path(os.path.dirname(os.path.abspath(__file__)),"StatsLogo1.png")))
        self.pixmap2=self.pixmap.scaled(self.logoWidth*.80,self.logoWidth*.80)
        
        self.label=QLabel(self)
        self.label.setPixmap(self.pixmap2)

        self.layout=QGridLayout()
        self.layout.addWidget(self.label)
        self.logoGroup.setLayout(self.layout)

    #Right side for the Expanding Label
    def createInfoGroup(self):
        self.infoGroup = QGroupBox("")
        self.infoGroup.setFixedWidth(self.infoWidth)
        self.infoLabel=QLabel(self)
        self.infoLabel.setStyleSheet("font: 15pt Tw Cen MT")
        self.infoLabel.setText("Welcome to the Stats Wiz!! Here's all you need to know:")
          
        window =CollapsibleDialog() #this create the Collapsible Dialog handler
        
        self.layout=QGridLayout()
        self.layout.addWidget(self.infoLabel)
        self.layout.addWidget(window)
        self.infoGroup.setLayout(self.layout)


class LabelExpandButton(QPushButton):
    #
    #A QPushButton that would expand or collapse its section
    #
    def __init__(self, item, text="", parent=None):
        super().__init__(text,parent)
        self.section=item
        self.clicked.connect(self.on_clicked)
    def on_clicked(self):#TODO: look here if reason that Sam got the glitch because of sizing problem?
        #
        #Toggle the section (expand/collapse) by clicking
        #
        if self.section.isExpanded():
            self.section.setExpanded(False)
        elif not self.section.isExpanded():
            self.section.setExpanded(True)
        else: #close it no matter want just in case it goes wrong
            self.section.setExpanded(False)

class CollapsibleDialog(QDialog):
    #
    #A Dialog to which collapsible sections can be added;
    #
    def __init__(self):
        super().__init__()
        self.tree=QTreeWidget()
        self.tree.setHeaderHidden(True)
        layout=QVBoxLayout()
        layout.addWidget(self.tree)
        self.setLayout(layout)
        self.tree.setIndentation(0)
        self.infoWidth=self.tree.size().width()
        print(self.infoWidth)
        self.sections=[]
        self.define_sections()
        self.add_sections()

    def add_sections(self):
        #adds a collapsible sections for every 
        #(title, widget) tuple in self.sections
        #
        for (title, widget) in self.sections:
            button1 = self.add_button(title)
            section1 = self.add_widget(button1, widget)
            section1.setFlags(section1.flags() & ~Qt.ItemIsSelectable)#deactivate label being selectable
            section1.setFlags(section1.flags() & ~Qt.ItemIsEnabled)
            section1.setFlags(section1.flags() & Qt.NoFocus)
            #section1.setFlags(section1 & QAbstractItemView.NoFocus)
            section1.setSelected(False)
            section1.setSelected(True)
            section1.setSelected(False)
            button1.addChild(section1)

    def define_sections(self):
        #reimplement this to define all your sections
        #and add them as (title, widget) tuples to self.sections
        #
        style =QLabel().setStyleSheet("font: 15pt Tw Cen MT")
        
        #    self.labelText = QLabel(self)
        widget = QFrame(self.tree)
        layout = QVBoxLayout(widget)
        
        infoD=QLabel(self)
        
        infoD.setStyleSheet("font: 15pt Tw Cen MT")
        infoD.setText("Data can be manually entered into a table or uploaded from a CSV File.\n"
                               "The first row will be for Headers\n"
                               "The rest of the capabilities will be dependent upon \nthe type of data you entered\n"
                               "(ordinal, interval, or frequency).\n\n"
                               "[Data]"
                               "\nChoice to Graph Everything\n"
                                "Specify certain rows and columns to perform analyses on.\n"    
                               "\n[Type]\n"
                               "Please specify if Data is Interval, Ordinal, or Frequency.\n\n"
                               "[Buttons]\n"
                               "Import CSV: Use a CSV file that already exist.\n"
                               "Clear Table: Remove the data completely from table.\n"
                               "Submit Data: Pass the data you plan to use for analysis.")
        # titleD=QLabel(self)
        # titleD.setStyleSheet("font 20pt Tw Cen MT")
        # titleD.setText("DataTab")
        
        layout.addWidget(infoD)
        title = "DataTab"
        self.sections.append((title, widget))


        widget = QFrame(self.tree)
        layout = QVBoxLayout(widget)
        infoG=QLabel(self)
        infoG.setStyleSheet("font: 15pt Tw Cen MT")
        infoG.setText("The graph will be selectable by the user for display.\n\n"
                               "[Selection]\n"
                               "Vertical Bar\n"
                               "Horizontal Bar\n"
                               "Pie Chart\n"
                                "Normal Distribution Curve\n"
                                "Scatter Plot\n\n"
                                "[Buttons]\n"
                                "Graph: Proceeds to graph data based on graph selection\n"
                                "Save as PNG: To save the graph generated as PNG")

        layout.addWidget(infoG)
        title = "GraphTab"
        self.sections.append((title, widget))

        #"[Interval Data Test]\n"
        #"Mean, Median, Mode, Standard Deviation, Least Square Line, X^2 (Chi Square),\n"
        #"Correlation Coefficient, Sign Test, Rank Sum Test, and Spearman Rank Correlation.\n\n"
        #"[Ordinal Data Test]\n"
        #"Mean, Median, Mode, Standard Deviation, Least Square Line, X^2 (Chi Square),\n"
        #"Correlation Coefficient, Sign Test, Rank Sum Test, and Spearman Rank Correlation.\n\n"
        #"[Frequency Data Test]\n"
        #"Mean, Median, Mode, Standard Deviation, Least Square Line, X^2 (Chi Square),\n"
        #"Correlation Coefficient, Sign Test, Rank Sum Test, and Spearman Rank Correlation.\n\n"    
                               
        widget = QFrame(self.tree)
        layout = QVBoxLayout(widget)
        infoA=QLabel(self)
        infoA.setStyleSheet("font: 15pt Tw Cen MT")
        infoA.setText("Apply Statistical Analysis if it is meaningful for the type of data.\n"
                                "May select more than one statistical test for any specified set of data.\n"
                                "The following statistical analyses on your data:\n" )

       
        infoA2 = QLabel(self)
        infoA2.setStyleSheet("font: 15pt Tw Cen MT")
        infoA2.setText("\n[Analyze]\n"
                                "Proceed to apply the Statistical Analysis that would be applied.")
       #picture of a table with test that apply for the type of data
        
        self.pixmap=QPixmap(os.path.join(Path(os.path.dirname(os.path.abspath(__file__)),"TableTest.JPG")))
        self.pixmap2=self.pixmap.scaled(self.infoWidth*.60,self.infoWidth*.50)
        pic=QLabel(self)
        pic.setPixmap(self.pixmap2)
        
        
        layout.addWidget(infoA)
        layout.addWidget(pic)
        layout.addWidget(infoA2)
        
        title = "AnalysisTab"
        self.sections.append((title, widget))
        
        widget = QFrame(self.tree)
        layout = QVBoxLayout(widget)
        infoS=QLabel(self)
        infoS.setStyleSheet("font: 15pt Tw Cen MT")
        infoS.setText("See a summary of all the results of all \nStatistical Analysis you did to your data.\n\n"
                        "[Options]\n"
                        "Save: User to save the Summary Report as text file.\n"
                        "Clear: User to clear the Summary Report Log.")
        layout.addWidget(infoS)
        title = "SummaryTab"
        self.sections.append((title, widget))

    def add_button(self, title):
        #creates a QTreeWidgetItem containing a button 
        #to expand or collapse its section
        #
        item = QTreeWidgetItem()
        self.tree.addTopLevelItem(item)
        self.tree.setItemWidget(item, 0, LabelExpandButton(item, text = title))
        return item

    def add_widget(self, button, widget):
        #creates a QWidgetItem containing the widget,
        #as child of the button-QWidgetItem
        #
        section = QTreeWidgetItem(button)
        section.setDisabled(False)
        section.setFlags(section.flags() & ~Qt.ItemIsSelectable)
        section.setFlags(section.flags() & ~Qt.ItemIsEnabled)
        section.setFlags(section.flags() & Qt.NoFocus)
        section.setSelected(False)
        section.setSelected(True)
        section.setSelected(False)
        self.tree.setItemWidget(section, 0, widget)
        return section

#TODO: WelcomeTab: CollapsibleBoxDoesnt do anything delete          
# class CollapsibleBox(QtWidgets.QWidget):
#         def __init__(self, title='', parent=None):
#             super(CollapsibleBox, self).__init__(parent)
#             self.toggle_select=QtWidgets.QToolButton(
#                 text=title, checkable=True, checked=False
#             )
#             self.toggle_select.setStyleSheet("QToolButton { border: none; }")
#             self.toggle_select.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
#             self.toggle_select.setArrowType(QtCore.Qt.RightArrow)
#             self.toggle_select.pressed.connect(self.clickedPressed)
#             self.toggle_animate=QtCore.QParallelAnimationGroup(self)
#             self.content_info=QtWidgets.QScrollArea(maximumHeight=0, minimumHeight=0)
#             self.content_info.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
#             self.content_info.setFrameShape(QtWidgets.QFrame.NoFrame)
#             layout=QtWidgets.QVBoxLayout(self)
#             layout.setSpacing(0)
#             layout.setContentsMargins(0,0,0,0)
#             layout.addWidget(self.toggle_select)
#             layout.addWidget(self.content_info)

#             self.toggle_animate.addAnimation(QtCore.QPropertyAnimation(self, b"minimumHeight"))
#             self.toggle_animate.addAnimation(QtCore.QPropertyAnimation(self, b"maximumHeight"))
#             self.toggle_animate.addAnimation(QtCore.QPropertyAnimation(self.content_info, b"maximumHeight"))

#         @QtCore.pyqtSlot()
#         def clickedPressed(self):
#             isChecked=self.toggle_select.isChecked()
#             self.toggle_select.setArrowType(QtCore.Qt.DownArrow if not isChecked else QtCore.Qt.RightArrow)
#             self.toggle_animate.setDirection(QtCore.QAbstractAnimation.Forward if not isChecked else QtCore.QAbstractAnimation.Backward)
#             self.toggle_animate.start()
#         def setContentLayout(self, layout):
#             lay=self.content_info.layout()
#             del lay
#             self.content_info.setLayout(layout)
#             collapsed_height=(self.sizeHint().height()-self.content_info.maximumHeight())
#             content_height = layout.sizeHint().height()
#             for i in range(self.toggle_animate.animationCount()):
#                 animation=self.toggle_animate.animationAt(i)
#                 animation.setDuration(500)
#                 animation.setStartValue(collapsed_height)
#                 animation.setEndValue(collapsed_height+content_height)
            
#             content_animation = self.toggle_animate.animationAt(self.toggle_animate.animationCount() -1)
#             content_animation.setDuration(500)
#             content_animation.setStartValue(0)
#             content_animation.setEndValue(content_height)
                

#"""



"""
from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QMainWindow, QPushButton, QDialog, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QHBoxLayout, QFrame, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random


#https://github.com/By0ute/pyqt-collapsible-widget

class WelcomeTab(QMainWindow):
    def __init__(self):
        super().__init__()
        

        
        self.centralWidget = QWidget()
        self.labelText = QLabel(self)
        self.infoText = QLabel(self)
        self.layout = QGridLayout()
        self.layoutCollaspse=QGridLayout()
        self.pixmap = QPixmap("src\GUI\StatsLogo1.png")
        self.pixmap2 = self.pixmap.scaled(600, 600)
        self.label = QLabel(self)
        self.initUi()    
        

    def initUi(self):
        
        self.createGridLayout()
        self.show()
        

    def createGridLayout(self):
        
        self.label.setPixmap(self.pixmap2)
        self.labelText.setText("Welcome to the Stats Wiz? Here's all you need to know:")
        
       
        
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

        
        self.layout.addWidget(self.labelText, 0, 1)#where to put the text
        self.layout.addWidget(self.label, 0, 0) #where to put the picture
        
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.layout)
        
        #"""