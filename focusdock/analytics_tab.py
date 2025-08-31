from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AnalyticsTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout(self)

        # Static message
        self.info_label = QLabel("Analytics overview")
        layout.addWidget(self.info_label)

        # Labels for stats
        self.task_ratio = QLabel()
        self.total_label = QLabel()
        self.completed_label = QLabel()
        self.uncompleted_label = QLabel()

        layout.addWidget(self.task_ratio)
        layout.addWidget(self.total_label)
        layout.addWidget(self.completed_label)
        layout.addWidget(self.uncompleted_label)

        self.setLayout(layout)

        # Initial update
        self.update_stats()

    def update_stats(self):
        tm = self.main_window.todo_manager

        # Avoid division by zero
        completed = tm.get_completed_tasks()
        total = tm.get_total_tasks()
        if total == 0:
            ratio = 0
        else:
            ratio = (completed / total) * 100

        self.task_ratio.setText(f"Task Completion Ratio: {ratio:.1f} %")

        self.total_label.setText(f"Total Tasks: {tm.get_total_tasks()}")
        self.completed_label.setText(f"Completed Tasks: {tm.get_completed_tasks()}")
        self.uncompleted_label.setText(f"Uncompleted Tasks: {tm.get_uncompleted_tasks()}")