# page1.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class Other(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("other"))
        self.setLayout(layout)
