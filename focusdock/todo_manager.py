from PyQt6.QtWidgets import QListWidget, QLineEdit

from focusdock.storage import load_settings, save_settings
from focusdock.analytics_tab import AnalyticsTab

class TodoManager:
    def __init__(self, todo_list_widget: QListWidget, todo_input_field: QLineEdit):
        self.tasks = []
        self.lt_total = 0
        self.total_completed = 0
        self.completed = 0
        self.todo_list_widget = todo_list_widget
        self.todo_input_field = todo_input_field
        
        self.load()

    def add_task(self, text: str):
        text = text.strip()
        if text:
            self.tasks.append(text)
            self.lt_total += 1
            self.todo_list_widget.addItem(text)
            self.todo_input_field.clear()
            self.save()

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.completed += 1
            self.total_completed += 1
            self.todo_list_widget.takeItem(index)
            self.save()

    def get_tasks(self) -> int:
        return len(self.tasks) + self.completed
    
    def get_total_tasks(self) -> int:
        return self.lt_total
    
    def get_total_complete_tasks(self) -> int:
        return self.total_completed

    def get_completed_tasks(self) -> int:
        return self.completed

    def get_current_tasks(self) -> int:
        return len(self.tasks)
    
    def save(self):
        data = load_settings()
        data["tasks"] = self.tasks
        data["lt_total"] = self.lt_total
        data["total_completed"] = self.total_completed
        save_settings(data)

    def load(self):
        data = load_settings()
        self.tasks = data.get("tasks", [])
        self.lt_total = data.get("lt_total", 0)
        self.total_completed = data.get("total_completed", 0)
        self.refresh_ui()

    def clear(self):
        self.completed = 0

    def refresh_ui(self):
        self.todo_list_widget.clear()
        for task in self.tasks:
            self.todo_list_widget.addItem(task)