import sys, os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QLineEdit, QSpinBox
)
from PyQt6.QtCore import QTimer
from PyQt6.QtCore import Qt


class FocusDock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FocusDock - MVP")
        self.setGeometry(100, 100, 400, 500)
        self.layout = QVBoxLayout()

        # Timer controls layout
        timer_layout = QHBoxLayout()
        timer_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        timer_layout.setSpacing(10)
        self.timer_label = QLabel("25:00")
        timer_layout.addWidget(self.timer_label)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)
        timer_layout.addWidget(self.start_button)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_timer)
        timer_layout.addWidget(self.reset_button)

        self.layout.addLayout(timer_layout)

        # Timer length selector
        length_layout = QHBoxLayout()
        length_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        length_layout.addWidget(QLabel("Minutes:"))
        self.timer_length_spin = QSpinBox()
        self.timer_length_spin.setMinimum(1)
        self.timer_length_spin.setMaximum(180)
        self.timer_length_spin.setValue(25)
        length_layout.addWidget(self.timer_length_spin)

        self.set_button = QPushButton("Set")
        self.set_button.clicked.connect(self.set_timer)
        length_layout.addWidget(self.set_button)

        self.layout.addLayout(length_layout)

        # To-do list input layout
        todo_input_layout = QHBoxLayout()
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Add a new task...")
        todo_input_layout.addWidget(self.todo_input)

        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)
        todo_input_layout.addWidget(add_button)
        self.layout.addLayout(todo_input_layout)

        # To-do list widget
        self.todo_list = QListWidget()
        self.layout.addWidget(self.todo_list)

        # Remove task button
        remove_button = QPushButton("Remove Selected Task")
        remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(remove_button)

        self.setLayout(self.layout)

        # Timer logic
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_left = self.timer_length_spin.value() * 60

        # Check timer status
        self.timer_running = False
        self.original_time = self.timer_length_spin.value() * 60
        self.time_left = self.original_time

    # Timer methods
    def start_timer(self):
        if self.timer_running:
            # Pause timer
            self.timer.stop()
            self.timer_running = False
            self.start_button.setText("Resume")
        else:
            # Start timer
            self.timer.start(1000)
            self.timer_running = True
            self.start_button.setText("Pause")

    def set_timer(self):
        self.timer.stop()
        self.timer_running = False
        self.original_time = self.timer_length_spin.value() * 60
        self.time_left = self.original_time
        self.update_timer_label()
        self.start_button.setText("Start")

    def reset_timer(self):
        self.timer.stop()
        self.timer_running = False
        self.time_left = self.original_time  # use original time, not spinbox
        self.update_timer_label()
        self.start_button.setText("Start")

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_timer_label()
        else:
            self.timer.stop()
            self.timer_label.setText("Time's up!")

    def update_timer_label(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")

    # To-do list methods
    def add_task(self):
        task_text = self.todo_input.text().strip()
        if task_text:
            self.todo_list.addItem(task_text)
            self.todo_input.clear()

    def remove_task(self):
        selected_items = self.todo_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.todo_list.takeItem(self.todo_list.row(item))

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # When running as a bundled app
        base_path = sys._MEIPASS
    except Exception:
        # When running normally
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Use resource_path to find style.qss
    qss_path = resource_path("style.qss")
    with open(qss_path, "r") as f:
        app.setStyleSheet(f.read())

    from focusdock import FocusDock
    window = FocusDock()
    window.show()
    sys.exit(app.exec())