from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AnalyticsTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout(self)

        # Static message
        self.info_label = QLabel("Analytics overview")
        layout.addWidget(self.info_label)

        # Lifetime Stats
        self.total_label = QLabel()
        self.overall_rating = QLabel()

        layout.addWidget(self.total_label)
        layout.addWidget(self.overall_rating)

        # Labels for stats
        self.task_ratio = QLabel()
        self.completed_label = QLabel()
        self.current_label = QLabel()

        layout.addWidget(self.task_ratio)
        layout.addWidget(self.completed_label)
        layout.addWidget(self.current_label)

        self.setLayout(layout)

        # Initial update
        self.update_stats()

    def update_stats(self):
        tm = self.main_window.todo_manager

        # Check for current ratio
        completed = tm.get_completed_tasks()
        total = tm.get_tasks()
        if total == 0:
            ratio = 0
        else:
            ratio = (completed / total) * 100

        # Check for overall rating
        total_complete = tm.get_total_complete_tasks()
        total_tasks = tm.get_total_tasks()

        if total_tasks == 0:
            rating = 0
        else:
            rating = (total_complete / total_tasks) * 5
            rating = round(rating, 1)

        self.total_label.setText(f"Total Lifetime Tasks: {tm.get_total_tasks()}")
        self.overall_rating.setText(f"Personal Rating: {rating}")

        self.task_ratio.setText(f"Current Completion Ratio: {ratio:.1f} %")
        self.completed_label.setText(f"Completed Tasks: {tm.get_completed_tasks()}")
        self.current_label.setText(f"Current Tasks: {tm.get_current_tasks()}")