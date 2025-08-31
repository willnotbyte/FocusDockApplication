class TodoManager:
    def __init__(self):
        self.tasks = []            # All tasks
        self.completed_tasks = 0   # Completed tasks

    def add_task(self, text, list_widget, input_field):
        text = text.strip()
        if text:
            self.tasks.append(text)
            list_widget.addItem(text)
            input_field.clear()

    def remove_task(self, list_widget):
        selected_items = list_widget.selectedItems()
        for item in selected_items:
            list_widget.takeItem(list_widget.row(item))
            self.completed_tasks += 1
            if item.text() in self.tasks:
                self.tasks.remove(item.text())

    def get_total_tasks(self):
        return len(self.tasks) + self.completed_tasks

    def get_uncompleted_tasks(self):
        return len(self.tasks)
