from PyQt6.QtWidgets import QListWidget, QLineEdit

class TodoManager:
    def __init__(self, todo_list_widget: QListWidget, todo_input_field: QLineEdit):
        self.tasks = []
        self.completed = 0
        self.todo_list_widget = todo_list_widget
        self.todo_input_field = todo_input_field

    def add_task(self, text: str):
        text = text.strip()
        if text:
            self.tasks.append(text)
            self.todo_list_widget.addItem(text)
            self.todo_input_field.clear()

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.completed += 1
            self.todo_list_widget.takeItem(index)

    def get_total_tasks(self) -> int:
        return len(self.tasks) + self.completed

    def get_completed_tasks(self) -> int:
        return self.completed

    def get_uncompleted_tasks(self) -> int:
        return len(self.tasks)
