# main.py
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QStackedWidget
from routes import load_route  # 导入加载路由的函数

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Routing Example with Init Registration")
        self.setGeometry(100, 100, 600, 400)

        # Create a stacked widget for routing
        self.stacked_widget = QStackedWidget()

        # Create pages dynamically from routes
        self.routes = ["home", "mine", "other"]
        self.pages = {route: load_route(route)() for route in self.routes}  # 实例化每个页面类

        # Add pages to stacked widget
        for page in self.pages.values():
            self.stacked_widget.addWidget(page)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Create navigation buttons
        self.create_navigation_buttons(main_layout)

    def create_navigation_buttons(self, layout):
        """Create navigation buttons for routing."""
        button_layout = QVBoxLayout()

        for path in self.routes:
            button = QPushButton(f"Go to {path.capitalize()}")
            button.clicked.connect(lambda _, p=path: self.navigate_to(p))
            button_layout.addWidget(button)

        # Add button layout to the main layout
        layout.addLayout(button_layout)

    def navigate_to(self, page_path):
        """Navigate to the specified page based on the path."""
        if page_path in self.routes:
            index = self.routes.index(page_path)
            self.stacked_widget.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
