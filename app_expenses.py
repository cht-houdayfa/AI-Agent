class Task:
    def __init__(self, title=None, due_date=None, due_time=None):
        self.title = title
        self.due_date = due_date
        self.due_time = due_time
        
class SchedulerApp:
    
    def __init__(self):
        self.tasks = []

    def add_task(self, title=None, due_date=None, due_time=None):
        new_task = Task(title, due_date, due_time)
        self.tasks.append(new_task)
        
    def display_sorted_tasks(self):  # Display tasks sorted by date and time in descending order
        self.tasks.sort(key=lambda x: (x.due_date, x.due_time), reverse=True)
        for task in self.tasks:
            print("Title: ", task.title, "Due Date: ", task.due_date, " Due Time: ", task.due_time)
            
    def change_task_time(self, title, new_due_time):  # Change the time for a specific task
        for task in self.tasks:
            if task.title == title:
                task.due_time = new_due_time