سوف يقوم خطوتي الكتابة الرياضية على التصميم النظيف البرمجي في الوقت المناسب.

```python
import tkinter as tk
from tkinter import messagebox, simpledialog
import pickle

class Task:
    def __init__(self, name, due_date, category):
        self.name = name
        self.due_date = due_date
        self.category = category
        self.done = False

class TasksApp:
    def __init__(self):
        self.tasks = []
        self.window = tk.Tk()
        self.create_widgets()
        self.load_data()  # load tasks from file if it exists

    def run(self):
        self.window.mainloop()

    def create_widgets(self):
        self.new_task = tk.Button(text="Add Task", command=self.add_task)
        self.new_task.pack()
        self.view_tasks = tk.Button(text="View Tasks", command=self.show_all_tasks)
        self.view_tasks.pack()
        self.delete_task = tk.Button(text="Delete Task", command=self.delete_task)
        self.delete_task.pack()

    def add_task(self):
        name = simpledialog.askstring("Task Name", "Enter task name")
        due_date = simpledialog.askstring("Due Date", "Enter the due date for this task")
        category = simpledialog.askstring("Category", "Enter a category for this task")
        new_task = Task(name, due_date, category)
        self.tasks.append(new_task)
        self.save_data()  # save tasks to file

    def show_all_tasks(self):
        for task in self.tasks:
            messagebox.showinfo("Task", f"Name: {task.name}\nDue Date: {task.due_date}\nCategory: {task.category}")

    def delete_task(self):
        index = int(simpledialog.askstring("Delete Task", "Enter the task number you want to delete")) - 1
        if index < len(self.tasks) and not self.tasks[index].done:
            messagebox.showinfo("Task Deleted", f"{self.tasks[index].name} has been deleted.")
            del self.tasks[index]
        else:
            messagebox.showerror("Invalid Index", "No task at that index or the task is already completed")
        self.save_data()  # save tasks to file

    def load_data(self):
        try:
            with open('tasks.pkl', 'rb') as f:
                self.tasks = pickle.load(f)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('tasks.pkl', 'wb') as f:
            pickle.dump(self.tasks, f)
```

هذا الكود يتم إنشاءه بناءً على المتطلبات المرجعة. لا يوجد حلقة الاستثناءات أو الأخطاء لضمان عدم انهيار التطبيق، ولكن لا تزال إن حدثنا من هذا الكود في مساحة العمل.