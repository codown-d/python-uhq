# page1.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class Mine(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("mine"))
        self.setLayout(layout)
