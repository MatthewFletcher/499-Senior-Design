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

        # self.dataTabText=QLabel(self)
        # self.graphTabText=QLabel(self)
        # self.analysisTabText=QLabel(self)
        # self.summaryTabText=QLabel(self)

        self.layout = QGridLayout()
      
        

        self.pixmap = QPixmap("StatsLogo1.png")
        self.pixmap2 = self.pixmap.scaled(600, 600)
        self.label = QLabel(self)
        self.initUi()
    
    def initUi(self):
        self.createGridLayout()
        self.show()

    def createGridLayout(self):
        self.label.setPixmap(self.pixmap2)
        #self.labelText.setText("Welcome to the Stats Wiz? Here's all you need to know:")
        

        window=CollapsibleDialog()
        
        self.layout.addWidget(window)
        

        """
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

        #"""
        self.layout.addWidget(self.labelText, 0, 1)#where to put the text
        self.layout.addWidget(self.label, 0, 0) #where to put the picture
        
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.layout)

class LabelExpandButton(QPushButton):
    """
    A QPushButton that would expand or collapse its section
    """
    def __init__(self, item, text="", parent=None):
        super().__init__(text,parent)
        self.section=item
        self.clicked.connect(self.on_clicked)
    def on_clicked(self):
        """
        Toggle the section (expand/collapse) by clicking
        """
        if self.section.isExpanded():
            self.section.setExpanded(False)
        else:
            self.section.setExpanded(True)

class CollapsibleDialog(QDialog):
    """
    A Dialog to which collapsible sections can be added;
    """
    def __init__(self):
        super().__init__()
        self.tree=QTreeWidget()
        self.tree.setHeaderHidden(True)
        layout=QVBoxLayout()
        layout.addWidget(self.tree)
        self.setLayout(layout)
        self.tree.setIndentation(0)

        self.sections=[]
        self.define_sections()
        self.add_sections()

    def add_sections(self):
        """adds a collapsible sections for every 
        (title, widget) tuple in self.sections
        """
        for (title, widget) in self.sections:
            button1 = self.add_button(title)
            section1 = self.add_widget(button1, widget)
            button1.addChild(section1)

    def define_sections(self):
        """reimplement this to define all your sections
        and add them as (title, widget) tuples to self.sections
        """

        widget = QFrame(self.tree)
        layout = QHBoxLayout(widget)
        layout.addWidget(QLabel("Data can be manually entered into a table or uploaded from a CSV File.\n"
                               "The rest of the capabilities will be dependent upon the type of data you entered\n"
                               "(ordinal, interval, or frequency)."))
        title = "DataTab"

        self.sections.append((title, widget))
        widget = QFrame(self.tree)
        layout = QHBoxLayout(widget)
        layout.addWidget(QLabel("Our application will graph your data with your choice of "
                               "graph-\nHorizontal bar chart, vertical bar chart, pie chart, normal distribution "
                               "curve, or X-Y graph."))
        title = "GraphTab"

        self.sections.append((title, widget))
        widget = QFrame(self.tree)
        layout = QHBoxLayout(widget)
        layout.addWidget(QLabel("We can run the following statistical analyses on your data-\nmean, "
                               "median, mode, standard deviation, variance, coefficient of variance,\npercentiles, "
                               "probability distribution, binomial distribution,\nleast square line, X^2 (Chi Square), "
                               "correlation coefficient, sign test,\nrank sum test, and Spearman rank correlation "
                               "coefficient."))
        title = "AnalysisTab"

        self.sections.append((title, widget))
        widget = QFrame(self.tree)
        layout = QHBoxLayout(widget)
        layout.addWidget(QLabel("Here you can see a summary of all you did to your data."))
        title = "SummaryTab"
        self.sections.append((title, widget))

    def add_button(self, title):
        """creates a QTreeWidgetItem containing a button 
        to expand or collapse its section
        """
        item = QTreeWidgetItem()
        self.tree.addTopLevelItem(item)
        self.tree.setItemWidget(item, 0, LabelExpandButton(item, text = title))
        return item

    def add_widget(self, button, widget):
        """creates a QWidgetItem containing the widget,
        as child of the button-QWidgetItem
        """
        section = QTreeWidgetItem(button)
        section.setDisabled(True)
        self.tree.setItemWidget(section, 0, widget)
        return section

            
# class CollapsibleBox(QtWidgets.QWidget):
#         def __init__(self, title='', parent=None):
#             super(CollapsibleBox, self).__init__(parent)
#             self.toggle_select=QtWidgets.QToolButton(
#                 text=title, checkable=True, checked=False
#             )
#             self.toggle_select.setStyleSheet("QToolButton { bordrer: none; }")
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