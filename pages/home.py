# page1.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class Home(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("home"))
        self.setLayout(layout)
