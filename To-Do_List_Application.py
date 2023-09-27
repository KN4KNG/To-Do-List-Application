import tkinter as tk
from tkinter import messagebox

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Create a list to store tasks and their completion status
tasks = []
task_status = []  # Keeps track of whether each task is complete (True) or not (False)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_status.append(False)  # Initialize task as not complete
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a task
def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        del tasks[index]
        del task_status[index]
        task_listbox.delete(index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to edit a task
def edit_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        edited_task = task_entry.get()
        if edited_task:
            tasks[index] = edited_task
            task_listbox.delete(index)
            task_listbox.insert(index, edited_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to edit.")

# Function to mark a task as complete
def mark_complete():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task_status[index] = True
        task_listbox.itemconfig(index, {'bg': 'light green'})
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")

# Function to reorder tasks
def move_up():
    selected_task_index = task_listbox.curselection()
    if selected_task_index and selected_task_index[0] > 0:
        index = selected_task_index[0]
        task = tasks[index]
        task_stat = task_status[index]
        del tasks[index]
        del task_status[index]
        tasks.insert(index - 1, task)
        task_status.insert(index - 1, task_stat)
        update_task_listbox()

# Function to move a task down in the list
def move_down():
    selected_task_index = task_listbox.curselection()
    if selected_task_index and selected_task_index[0] < len(tasks) - 1:
        index = selected_task_index[0]
        task = tasks[index]
        task_stat = task_status[index]
        del tasks[index]
        del task_status[index]
        tasks.insert(index + 1, task)
        task_status.insert(index + 1, task_stat)
        update_task_listbox()

# Function to update the task listbox
def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for i, (task, stat) in enumerate(zip(tasks, task_status)):
        task_listbox.insert(tk.END, task)
        if stat:
            task_listbox.itemconfig(i, {'bg': 'light green'})

# Create and configure widgets
task_label = tk.Label(app, text="Task:")
task_entry = tk.Entry(app, width=30)
add_button = tk.Button(app, text="Add", command=add_task, width=15)
remove_button = tk.Button(app, text="Remove", command=remove_task, width=15)
edit_button = tk.Button(app, text="Edit", command=edit_task, width=15)
mark_complete_button = tk.Button(app, text="Mark Complete", command=mark_complete, width=15)
move_up_button = tk.Button(app, text="Move Up", command=move_up, width=15)
move_down_button = tk.Button(app, text="Move Down", command=move_down, width=15)
task_listbox = tk.Listbox(app, width=50, height=10, selectmode=tk.SINGLE)

# Grid layout for buttons and labels
task_label.grid(row=0, column=0, padx=2, pady=10)
task_entry.grid(row=0, column=1, padx=10, pady=10)
add_button.grid(row=1, column=0, padx=2, pady=2)
remove_button.grid(row=2, column=0, padx=2, pady=2)
edit_button.grid(row=1, column=1, padx=2, pady=2)
mark_complete_button.grid(row=2, column=1, padx=2, pady=2)
move_up_button.grid(row=1, column=2, padx=2, pady=2)
move_down_button.grid(row=2, column=2, padx=2, pady=2)
task_listbox.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# Function to close the application
def close_app():
    app.destroy()

# Add a menu
menu = tk.Menu(app)
app.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=close_app)

# Start the GUI main loop
app.mainloop()
