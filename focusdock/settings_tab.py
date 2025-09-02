from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QComboBox,
    QLabel, QPushButton, QLineEdit
)

from focusdock.styles import apply_profile
from focusdock.storage import load_settings, save_settings, clear_save

class SettingsTab(QWidget):

    # Style path
    profile_path = "default.qss"

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout(self)

        # Savedata
        self.increments = 0
        self.username = "user"
        self.current_profile = "default.qss"

        # Static message
        self.info_label = QLabel("Settings overview")
        self.user_label = QLabel(f"User: {self.username}")

        self.set_usr_field = QLineEdit()
        self.set_usr_field.setPlaceholderText("Enter username...")

        self.set_usr_btn = QPushButton("Set")
        self.set_usr_btn.clicked.connect(self.set_username)

        self.theme_label = QLabel("Theme Profile: ")
        self.theme_dropdown = QComboBox()
        self.theme_dropdown.addItems(["default.qss", "style2.qss"])
        self.theme_dropdown.currentIndexChanged.connect(self.on_selection_change)

        layout.addWidget(self.info_label)
        layout.addWidget(self.user_label)
        layout.addWidget(self.set_usr_field)
        layout.addWidget(self.set_usr_btn)
        layout.addWidget(self.theme_label)
        layout.addWidget(self.theme_dropdown)

        # Analytics data
        self.increment_label = QLabel()
        self.reset_inc_btn = QPushButton("Clear Data")
        self.reset_inc_btn.clicked.connect(self.clear_data)
        layout.addWidget(self.increment_label)
        layout.addWidget(self.reset_inc_btn)

        # Save data
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        # Load settings from JSON
        self.load()

        # Initial update
        self.update_stats()

    def update_stats(self):
        self.increment_label.setText(f"Lifetime Sessions: {self.increments}")
        self.user_label.setText(f"User: {self.username}")
        self.theme_label.setText(f"Theme Profile: {self.current_profile}")
        self.theme_dropdown.setCurrentText(self.current_profile)

    def add_increment(self):
        self.increments += 1
        self.update_stats()
        self.save()

    def clear_data(self):
        clear_save()
        self.load()
        # reset timer
        # set timer to default
        # set timer field to default
        self.main_window.full_timer_reset()
        self.main_window.todo_manager.clear()
        self.main_window.todo_manager.load()
        self.main_window.analytics.update_stats()
        apply_profile(self.current_profile)

    def set_username(self):
        self.username = self.set_usr_field.text()
        self.set_usr_field.setText("")
        self.update_stats()
        self.save()

    def on_selection_change(self):
        self.current_profile = self.theme_dropdown.currentText()
        self.profile_path = self.current_profile
        apply_profile(self.profile_path)
        self.update_stats()
    
    def save(self):
        data = load_settings()
        data["username"] = self.username
        data["theme"] = self.current_profile
        data["sessions"] = self.increments
        save_settings(data)
    
    def load(self):
        settings = load_settings()
        self.username = settings.get("username", "user")
        self.current_profile = settings.get("theme", "default.qss")
        self.profile_path = self.current_profile
        self.increments = settings.get("sessions", 0)

        self.update_stats()
        