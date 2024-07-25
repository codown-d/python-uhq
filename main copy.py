import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('ui/page/main/main.ui', self)
        self.setup_ui()
        self.setWindowIcon(QIcon('resources/react.svg'))     
        self.load_stylesheet()

    def load_stylesheet(self):
        # Load the .qss file
        with open('ui/page/main/main.qss', 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
    def setup_ui(self):
        # 设置 UI 的初始状态或连接信号和槽
        self.button.clicked.connect(self.on_button_click)
    def on_button_click(self):
        self.label.setText("Button Clicked!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
