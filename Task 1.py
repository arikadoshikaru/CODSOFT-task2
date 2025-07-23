import tkinter as tk
from tkinter import messagebox, simpledialog
import time

# Yeh code ek simple To-Do List application banata hai jisme tasks add, edit, delete aur complete/uncomplete kiye ja sakte hain.
class TodoApp:
    def __init__(self, master):
        self.master = master
        self.tasks = []  # Yeh list mein tasks store honge
        master.title("Tasks")
        master.configure(bg="light green") 

        # Title label
        tk.Label(master, text="To-Do List", font=("Arial", 30, "bold"), bg="yellow").pack()

        # Input frame jahan user task enter karega
        input_frame = tk.Frame(master, bg="white")
        input_frame.pack(padx=0, pady=10)

        # Task entry box
        self.task_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.task_entry.pack(side="left", padx=(0, 5))
        self.task_entry.bind("<Return>", lambda e: self.add_task())  # Press karne se task add ho jaye

        # Add button to add new task
        tk.Button(input_frame, text="Add", command=self.add_task,
                  bg="green", fg="white", font=("Arial", 10, "bold"),
                  width=8).pack(side="left")

        # Frame jahan tasks display honge
        self.task_list_frame = tk.Frame(master, bg="white")
        self.task_list_frame.pack(expand=True, fill="both", padx=10, pady=(0, 10))

        self.display_tasks() 

    # Tasks ko GUI mein display karta hai
    def display_tasks(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()  

        if not self.tasks:
            tk.Label(self.task_list_frame, text="No tasks added yet!",
                     font=("Arial", 11, "italic"), bg="white").pack(pady=20)
            return

        for index, task in enumerate(self.tasks):
            task_frame = tk.Frame(self.task_list_frame, bg="white", bd=1, relief="solid")
            task_frame.pack(fill="x", pady=3)

            # Checkbox to mark task complete/incomplete
            tk.Checkbutton(task_frame, variable=tk.BooleanVar(value=task['completed']),
                           command=lambda i=index: self.toggle_complete(i),
                           bg="white").pack(side="left", padx=5)

            # Task description aur time dikhane ke liye
            text_section = tk.Frame(task_frame, bg="white")
            text_section.pack(side="left", expand=True, fill="x")

            font_style = ("Arial", 11, "overstrike" if task['completed'] else "normal")
            tk.Label(text_section, text=task['description'], font=font_style,
                     bg="white").pack(anchor="w", padx=5)

            # Timestamp - kab add aur complete hua
            timestamp = f"Added: {task['created_at']}"
            if task['completed_at']:
                timestamp += f" | Done: {task['completed_at']}"
            tk.Label(text_section, text=timestamp, font=("Arial", 8),
                     bg="white", fg="gray").pack(anchor="w", padx=5)

            # Buttons - edit aur delete ke liye
            action_frame = tk.Frame(task_frame, bg="white")
            action_frame.pack(side="right", padx=5)

            tk.Button(action_frame, text="Edit", command=lambda i=index: self.edit_task(i),
                      font=("Arial", 9), bg="blue", fg="white", width=5).pack(side="left", padx=1)

            tk.Button(action_frame, text="Del", command=lambda i=index: self.delete_task(i),
                      font=("Arial", 9), bg="red", fg="white", width=5).pack(side="left", padx=1)

    # Task add karta hai list mein
    def add_task(self):
        description = self.task_entry.get().strip()
        if description:
            new_task = {
                "description": description,
                "completed": False,
                "created_at": time.strftime('%Y-%m-%d %H:%M:%S'),
                "completed_at": None
            }
            self.tasks.append(new_task)
            print(f"Task added: {description}")
            self.task_entry.delete(0, tk.END)
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")  # Empty task nahi chalega

    # Complete status toggle karta hai task ka
    def toggle_complete(self, index):
        task = self.tasks[index]
        task['completed'] = not task['completed']
        task['completed_at'] = time.strftime('%Y-%m-%d %H:%M:%S') if task['completed'] else None
        status = "Completed" if task['completed'] else "Marked as pending"
        print(f"{status}: {task['description']}")
        self.display_tasks()

    # Task ko edit karne ka option deta hai
    def edit_task(self, index):
        current_description = self.tasks[index]['description']
        new_description = simpledialog.askstring("Edit Task", "Update the task:", initialvalue=current_description)
        if new_description and new_description.strip():
            self.tasks[index]['description'] = new_description.strip()
            print(f"Task updated: {new_description.strip()}")
            self.display_tasks()
        elif new_description is not None:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    # Task delete karta hai
    def delete_task(self, index):
        description = self.tasks[index]['description']
        if messagebox.askyesno("Delete", f"Delete '{description}'?"):
            print(f"Deleted task: {description}")
            del self.tasks[index]
            self.display_tasks()

# App ko launch karne wala code
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.geometry("500x600")  # Window size set kiya
    root.mainloop()