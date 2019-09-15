from PyQt5.QtWidgets import (QApplication,
QLabel,  QPushButton, QGridLayout, QWidget)
from PyQt5.QtGui import QPixmap

class StartPage(QWidget):
    def __init__(self):
        super().__init__()

        app = QApplication([])
        app.setStyle("Fusion")
        window = QWidget()

        label = QLabel
        label.setPixmap(QLabel(), QPixmap("StatsLogo1.png"))

        layout = QGridLayout()
        layout.addWidget(QPushButton("Import CSV File"))
        layout.addWidget(QPushButton("Manual Input"))
        layout.addWidget(QPushButton("Help"))

        window.setWindowTitle("Stats Wiz Start Page")
        window.setLayout(layout)
        window.show()
        app.exec_()
    
StartPage()