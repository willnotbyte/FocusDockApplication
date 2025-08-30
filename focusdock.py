import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QPushButton, QListWidget, QLineEdit, QHBoxLayout
)
from PyQt6.QtCore import QTimer

class FocusDock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FocusDock - MVP")
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout()

        # Timer
        self.timer_label = QLabel("25:00")
        self.layout.addWidget(self.timer_label)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)
        self.layout.addWidget(self.start_button)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_timer)
        self.layout.addWidget(self.reset_button)

        # To-Do List
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Add a new task...")
        self.layout.addWidget(self.todo_input)

        add_button = QPushButton("Add Task");
        add_button.clicked.connect(self.add_task)
        self.layout.addWidget(add_button)

        self.todo_list = QListWidget()
        self.layout.addWidget(self.todo_list)

        self.setLayout(self.layout)

        # Timer logic
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_left = 25 * 60 # 25 minutes

    # Timer methods
    def start_timer(self):
        self.timer.start(1000) # 1 second
    
    def reset_timer(self):
        self.timer.stop()
        self.time_left = 25 * 60 # 25 minutes
        self.update_timer_label()

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FocusDock()
    window.show()
    sys.exit(app.exec())