import tkinter as tk
from tkinter import messagebox

from task_manager.manager import (
    add_task,
    list_tasks,
    mark_task_done,
    delete_task
)

# 🎨 Pink palette
BG_COLOR = "#f8c8dc"
BTN_COLOR = "#f4a6c1"
ENTRY_BG = "#fff0f6"
LIST_BG = "#ffe6f0"
TEXT_COLOR = "#3a3a3a"
ACTIVE_BTN = "#f2b6cf"


class TaskManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.configure(bg=BG_COLOR)

        # Task title entry
        self.title_entry = tk.Entry(
            root, width=40, bg=ENTRY_BG, fg=TEXT_COLOR
        )
        self.title_entry.pack(pady=6)

        # Buttons
        tk.Button(
            root, text="Add Task",
            command=self.add_task_ui,
            bg=BTN_COLOR, fg=TEXT_COLOR,
            activebackground=ACTIVE_BTN
        ).pack(pady=2)

        tk.Button(
            root, text="Refresh Tasks",
            command=self.refresh_tasks,
            bg=BTN_COLOR, fg=TEXT_COLOR,
            activebackground=ACTIVE_BTN
        ).pack(pady=2)

        # Task ID entry
        self.id_entry = tk.Entry(
            root, width=10, bg=ENTRY_BG, fg=TEXT_COLOR
        )
        self.id_entry.pack(pady=6)

        tk.Button(
            root, text="Mark Done",
            command=self.mark_done_ui,
            bg=BTN_COLOR, fg=TEXT_COLOR,
            activebackground=ACTIVE_BTN
        ).pack(pady=2)

        tk.Button(
            root, text="Delete Task",
            command=self.delete_task_ui,
            bg=BTN_COLOR, fg=TEXT_COLOR,
            activebackground=ACTIVE_BTN
        ).pack(pady=2)

        # 📜 Frame for Listbox + Scrollbar
        list_frame = tk.Frame(root, bg=BG_COLOR)
        list_frame.pack(pady=10)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox = tk.Listbox(
            list_frame,
            width=60,
            bg=LIST_BG,
            fg=TEXT_COLOR,
            selectbackground=BTN_COLOR,
            yscrollcommand=scrollbar.set
        )
        self.task_listbox.pack(side=tk.LEFT)

        scrollbar.config(command=self.task_listbox.yview)

        self.refresh_tasks()

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        tasks = list_tasks()

        if not tasks:
            self.task_listbox.insert(tk.END, "No tasks found.")
            return

        for task in tasks:
            status = "✔" if task["done"] else "✗"
            self.task_listbox.insert(
                tk.END,
                f"[{task['id']}] {task['title']} - {status}"
            )

    def add_task_ui(self):
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showwarning("Error", "Task title cannot be empty")
            return

        add_task(title)
        self.title_entry.delete(0, tk.END)
        self.refresh_tasks()

    def mark_done_ui(self):
        try:
            task_id = int(self.id_entry.get())
            result = mark_task_done(task_id)
            if not result:
                messagebox.showwarning("Error", "Task not found")
        except ValueError:
            messagebox.showwarning("Error", "Enter a valid task ID")

        self.refresh_tasks()

    def delete_task_ui(self):
        try:
            task_id = int(self.id_entry.get())
            delete_task(task_id)
        except ValueError:
            messagebox.showwarning("Error", "Enter a valid task ID")

        self.refresh_tasks()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerUI(root)
    root.mainloop()
