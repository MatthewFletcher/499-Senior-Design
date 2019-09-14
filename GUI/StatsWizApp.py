from PyQt5.QtWidgets import (QApplication, QDialog, QTabWidget, 
QWidget, QVBoxLayout, QDialogButtonBox, QLabel, QLineEdit, QGroupBox,
QCheckBox, QComboBox, QListWidget)
from PyQt5.QtGui import QIcon
import sys 

class TabWdiget(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stats Wiz")
        self.setWindowIcon(QIcon("StatsLogo1.png"))

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

        name = QLabel("Name:")
        nameEdit = QLineEdit()

        dob = QLabel("Birth Date:")
        dobEdit = QLineEdit()

        phone = QLabel("Phone Number:")
        phoneEdit = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(name)
        layout.addWidget(nameEdit)
        layout.addWidget(dob)
        layout.addWidget(dobEdit)
        self.setLayout(layout)

class GraphTab(QWidget):
    def __init__(self):
        super().__init__()

        selectGroup = QGroupBox("Select Operating Systems")
        combo = QComboBox()
        list = ["Windows", "Mac", "Linux", "Fedora", "Kali"]
        combo.addItems(list)
        selectLayout = QVBoxLayout()
        selectLayout.addWidget(combo)
        selectGroup.setLayout(selectLayout)

        checkGroup = QGroupBox("Which Operating System Do You Like?")
        windows = QCheckBox("Windows")
        mac = QCheckBox("Mac")
        linux = QCheckBox("Linux")

        checkLayout = QVBoxLayout()
        checkLayout.addWidget(windows)
        checkLayout.addWidget(mac)
        checkLayout.addWidget(linux)

        checkGroup.setLayout(checkLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(selectGroup)
        mainLayout.addWidget(checkGroup)
        self.setLayout(mainLayout)

class AnalysisTab(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Terms and Conditions")
        listWidget = QListWidget()
        list = []

        for i in range(1, 20):
            list.append("This is the Terms and Conditions")

        listWidget.insertItems(1, list)

        checkbox = QCheckBox("Agree to the Terms and Conditions")

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(checkbox)
        self.setLayout(layout)

class SummaryTab(QWidget):
    def __init__(self):
        super().__init__()




app = QApplication(sys.argv)
tabwidget = TabWdiget()
tabwidget.show()
app.exec()