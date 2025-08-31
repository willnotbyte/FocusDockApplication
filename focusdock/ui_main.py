import sys, os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QListWidget, QLineEdit, QSpinBox,
    QMessageBox, QTabWidget, QApplication, QTimeEdit
)
from PyQt6.QtCore import QTimer, Qt, QTime
from focusdock.todo_manager import TodoManager

class FocusDock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FocusDock - MVP")
        self.resize(600, 800)

        # Timer variables
        self.original_time = 25 * 60
        self.time_left = self.original_time
        self.timer_running = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        # Task manager
        self.todo_manager = TodoManager()

        # Main layout & tabs
        self.main_layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.main_layout.addWidget(self.tabs)

        # --- Focus tab ---
        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout(self.tab1)
        self.tabs.addTab(self.tab1, "Focus")

        # Timer display + controls
        timer_layout = QHBoxLayout()
        timer_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_label = QLabel("25:00")
        timer_layout.addWidget(self.timer_label)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)
        timer_layout.addWidget(self.start_button)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_timer)
        timer_layout.addWidget(self.reset_button)
        self.tab1_layout.addLayout(timer_layout)

        # Timer length input (minutes + seconds)
        length_layout = QHBoxLayout()
        length_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_input = QTimeEdit()
        self.timer_input.setDisplayFormat("mm:ss")
        self.timer_input.setFixedWidth(80)
        length_layout.addWidget(QLabel("Set Timer:"))
        length_layout.addWidget(self.timer_input)
        
        self.set_button = QPushButton("Set")
        self.set_button.clicked.connect(self.set_timer)
        length_layout.addWidget(self.set_button)
        self.tab1_layout.addLayout(length_layout)

        # To-do list input
        todo_input_layout = QHBoxLayout()
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Add a new task...")
        todo_input_layout.addWidget(self.todo_input)

        add_button = QPushButton("Add Task")
        add_button.clicked.connect(lambda: self.todo_manager.add_task(self.todo_input.text(), self.todo_list, self.todo_input))
        todo_input_layout.addWidget(add_button)
        self.tab1_layout.addLayout(todo_input_layout)

        # To-do list widget
        self.todo_list = QListWidget()
        self.tab1_layout.addWidget(self.todo_list)

        # Remove task button
        remove_button = QPushButton("Remove Selected Task")
        remove_button.clicked.connect(lambda: self.todo_manager.remove_task(self.todo_list))
        self.tab1_layout.addWidget(remove_button)

        # --- Analytics tab ---
        self.tab2 = QWidget()
        self.tab2_layout = QVBoxLayout(self.tab2)
        self.tabs.addTab(self.tab2, "Analytics")

        self.analytics_label = QLabel("Analytics will go here")
        self.tab2_layout.addWidget(self.analytics_label)

    # ------------------ Timer Methods ------------------
    def start_timer(self):
        if self.timer_running:
            self.timer.stop()
            self.timer_running = False
            self.start_button.setText("Resume")
        else:
            self.timer.start(1000)
            self.timer_running = True
            self.start_button.setText("Pause")

    def set_timer(self):
        time = self.timer_input.time()
        self.original_time = time.minute() * 60 + time.second()
        self.time_left = self.original_time
        self.update_timer_label()
        self.start_button.setText("Start")
        self.timer.stop()
        self.timer_running = False

    def reset_timer(self):
        self.timer.stop()
        self.timer_running = False
        self.time_left = self.original_time
        self.update_timer_label()
        self.start_button.setText("Start")

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_timer_label()
        else:
            self.timer_finished()

    def update_timer_label(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")

    def timer_finished(self):
        uncompleted = self.todo_manager.get_uncompleted_tasks()
        completed = self.todo_manager.completed_tasks
        self.reset_timer()
        msg = QMessageBox()
        msg.setWindowTitle("Timer Alert")
        if uncompleted != 0:
            msg.setText(f"Your timer has finished! You have finished {completed} tasks! You still have {uncompleted} tasks to go!")
        else:
            msg.setText(f"Your timer has finished! You have finished all {completed} tasks! Great job!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
