from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class SettingsTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout(self)

        # Keep track of increments
        self.increments = 0

        # Static message
        self.info_label = QLabel("Settings overview")
        layout.addWidget(self.info_label)

        self.increment_label = QLabel()
        self.reset_inc_btn = QPushButton("Reset Analytics")
        self.reset_inc_btn.clicked.connect(self.reset_analytics)

        layout.addWidget(self.increment_label)
        layout.addWidget(self.reset_inc_btn)

        self.setLayout(layout)

        # Initial update
        self.update_stats()

    def update_stats(self):
        self.increment_label.setText(f"Life-Time Sessions: {self.increments}")

    def add_increment(self):
        self.increments += 1
        self.update_stats()

    def reset_analytics(self):
        self.increments = 0
        self.update_stats()