from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

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

        layout.addWidget(self.increment_label)

        self.setLayout(layout)

        # Initial update
        self.update_stats()

    def update_stats(self):
        self.increment_label.setText(f"Life-Time Sessions: {self.increments}")

    def add_increment(self):
        self.increments += 1
        self.update_stats()

    def reset_increments(self):
        self.increments = 0