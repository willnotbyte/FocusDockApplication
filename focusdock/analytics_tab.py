from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AnalyticsTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout(self)

        self.label = QLabel("Analytics will go here")
        layout.addWidget(self.label)

        # You can later add matplotlib or PyQtGraph plots here
