from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QLineEdit, QHBoxLayout, QLabel, QSpinBox

from PyQt6.QtCore import QTimer, Qt

class TodoManager(QWidget):
    def __init__(self):
        super().__init__()
        
        # Task analytics
        self.total_tasks = 0
        self.uncompleted_tasks = 0
        self.completed_tasks = 0

        # ---- First tab: Focus ----
        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout(self.tab1)
        self.tabs.addTab(self.tab1, "Focus")

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
        self.tab1_layout.addLayout(timer_layout)

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
        self.tab1_layout.addLayout(length_layout)

        # To-do list input layout
        todo_input_layout = QHBoxLayout()
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Add a new task...")
        todo_input_layout.addWidget(self.todo_input)

        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)
        todo_input_layout.addWidget(add_button)
        self.tab1_layout.addLayout(todo_input_layout)

        # To-do list widget
        self.todo_list = QListWidget()
        self.tab1_layout.addWidget(self.todo_list)

        # Remove task button
        remove_button = QPushButton("Remove Selected Task")
        remove_button.clicked.connect(self.remove_task)
        self.tab1_layout.addWidget(remove_button)

        # Timer logic
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_left = self.timer_length_spin.value() * 60

        # Check timer status
        self.timer_running = False
        self.original_time = self.timer_length_spin.value() * 60
        self.time_left = self.original_time

    def add_task(self):
        task = self.input.text()
        if task.strip() == "":
            return

        self.list.addItem(task)
        self.total_tasks += 1
        self.input.clear()

    def update_stats(self, item):
        # Here you’d handle marking tasks complete or incomplete
        pass
