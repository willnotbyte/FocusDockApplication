from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QLineEdit, QSpinBox,
    QMessageBox, QTabWidget, QApplication
)
from PyQt6.QtCore import QTimer, Qt
from focusdock.analytics_tab import AnalyticsTab

class FocusDock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FocusDock - MVP")
        self.resize(600, 800)

        # Task analytics
        self.total_tasks = 0
        self.completed_tasks = 0
        self.uncompleted_tasks = 0

        # Center window
        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()
        x = (screen_size.width() - self.width()) // 2
        y = (screen_size.height() - self.height()) // 2
        self.setGeometry(x, y, self.width(), self.height())

        # Main layout and tabs
        self.main_layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.main_layout.addWidget(self.tabs)

        # ---- Focus Tab ----
        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout(self.tab1)
        self.tabs.addTab(self.tab1, "Focus")
        self._setup_focus_tab()

        # ---- Analytics Tab ----
        self.tab2 = AnalyticsTab(self)
        self.tabs.addTab(self.tab2, "Analytics")

    def _setup_focus_tab(self):
        # Timer layout
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

        # Timer length
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
        self.tab1_layout.addLayout(length_layout)

        # Todo input
        todo_input_layout = QHBoxLayout()
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Add a new task...")
        todo_input_layout.addWidget(self.todo_input)

        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)
        todo_input_layout.addWidget(add_button)
        self.tab1_layout.addLayout(todo_input_layout)

        # Todo list
        self.todo_list = QListWidget()
        self.tab1_layout.addWidget(self.todo_list)

        remove_button = QPushButton("Remove Selected Task")
        remove_button.clicked.connect(self.remove_task)
        self.tab1_layout.addWidget(remove_button)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer_running = False
        self.original_time = self.timer_length_spin.value() * 60
        self.time_left = self.original_time

    # ---------------- Timer Methods ----------------
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
        self.timer.stop()
        self.timer_running = False
        self.original_time = self.timer_length_spin.value() * 60
        self.time_left = self.original_time
        self.update_timer_label()
        self.start_button.setText("Start")

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

    # ---------------- Task Methods ----------------
    def add_task(self):
        task_text = self.todo_input.text().strip()
        if task_text:
            self.total_tasks += 1
            self.todo_list.addItem(task_text)
            self.todo_input.clear()

    def remove_task(self):
        selected_items = self.todo_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.todo_list.takeItem(self.todo_list.row(item))
            self.completed_tasks += 1

    def timer_finished(self):
        self.uncompleted_tasks = self.total_tasks - self.completed_tasks
        self.reset_timer()
        msg = QMessageBox()
        msg.setWindowTitle("Timer Alert")
        if self.uncompleted_tasks != 0:
            msg.setText(
                f"Your timer has finished! You have finished {self.completed_tasks} tasks! "
                f"You still had {self.uncompleted_tasks} tasks to go, great work so far!"
            )
        else:
            msg.setText(f"Your timer has finished! You have finished all {self.completed_tasks} tasks! Great job!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
