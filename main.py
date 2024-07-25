import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLabel

class StackedWidgetExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Stacked Widget Example')

        # 创建主布局
        main_layout = QVBoxLayout()

        # 创建一个 QStackedWidget
        self.stacked_widget = QStackedWidget()

        # 创建第一个页面
        page1 = QWidget()
        page1_layout = QVBoxLayout()
        page1_layout.addWidget(QLabel('This is Page 1'))
        page1.setLayout(page1_layout)
        
        # 创建第二个页面
        page2 = QWidget()
        page2_layout = QVBoxLayout()
        page2_layout.addWidget(QLabel('This is Page 2'))
        page2.setLayout(page2_layout)
        
        # 创建第三个页面
        page3 = QWidget()
        page3_layout = QVBoxLayout()
        page3_layout.addWidget(QLabel('This is Page 3'))
        page3.setLayout(page3_layout)
        
        # 将页面添加到 QStackedWidget 中
        self.stacked_widget.addWidget(page1)
        self.stacked_widget.addWidget(page2)
        self.stacked_widget.addWidget(page3)

        # 创建按钮布局
        button_layout = QHBoxLayout()
        btn1 = QPushButton('Page 1')
        btn1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        button_layout.addWidget(btn1)

        btn2 = QPushButton('Page 2')
        btn2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        button_layout.addWidget(btn2)

        btn3 = QPushButton('Page 3')
        btn3.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        button_layout.addWidget(btn3)

        # 将按钮布局和 QStackedWidget 添加到主布局
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.stacked_widget)

        self.setLayout(main_layout)

app = QApplication(sys.argv)
window = StackedWidgetExample()
window.show()
sys.exit(app.exec_())
