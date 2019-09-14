from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,DialogButtonBox, QFormLayout, QGridLayout, QGroupBox, 
QHBoxLayout, QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QVBoxLayout, QWidget)
from PyQt5.QtGui import QPixmap

def StartPage():
    app = QApplication([])
    app.setStyle("Fusion")
    window = QWidget()

    label = QLabel
    label.setPixmap(QLabel(), QPixmap("StatsLogo1.png"))

    layout = QVBoxLayout()
    layout.addWidget(QPushButton("Import CSV File"))
    layout.addWidget(QPushButton("Manual Input"))
    layout.addWidget(QPushButton("Help"))

    window.setWindowTitle("Stats Wiz Start Page")
    window.setLayout(layout)
    window.show()
    app.exec_()
    
StartPage()