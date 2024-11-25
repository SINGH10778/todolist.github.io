import tkinter as tk
from tkinter import messagebox

# Function to add task to the list
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete selected task
def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark selected task as completed
def mark_completed():
    try:
        task_index = task_listbox.curselection()[0]
        task = task_listbox.get(task_index)
        task_listbox.delete(task_index)
        task_listbox.insert(task_index, f"{task} (Completed)")
        task_listbox.itemconfig(task_index, {'bg':'#D3F8D3'})
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Function to clear all tasks
def clear_all():
    task_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("450x500")
root.config(bg="#f0f4f8")

# Add a title label with a modern font and styling
title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 24, "bold"), fg="#2C3E50", bg="#f0f4f8")
title_label.pack(pady=20)

# Create the task entry field with modern styling
task_entry = tk.Entry(root, font=("Helvetica", 14), width=35, bd=2, relief="solid", highlightthickness=2, highlightcolor="#3498DB")
task_entry.pack(pady=10)

# Add button to add task with enhanced styling
add_button = tk.Button(root, text="Add Task", font=("Helvetica", 14), command=add_task, bg="#3498DB", fg="white", relief="flat", width=20)
add_button.pack(pady=5)

# Create a Listbox to display tasks with updated styling
task_listbox = tk.Listbox(root, font=("Helvetica", 14), width=35, height=10, selectmode=tk.SINGLE, bd=2, relief="solid", bg="#ffffff", fg="#2C3E50", highlightthickness=2, highlightcolor="#3498DB")
task_listbox.pack(pady=10)

# Add buttons with custom styles
delete_button = tk.Button(root, text="Delete Task", font=("Helvetica", 14), command=delete_task, bg="#E74C3C", fg="white", relief="flat", width=20)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark as Completed", font=("Helvetica", 14), command=mark_completed, bg="#2ECC71", fg="white", relief="flat", width=20)
mark_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", font=("Helvetica", 14), command=clear_all, bg="#F39C12", fg="white", relief="flat", width=20)
clear_button.pack(pady=5)

# Start the main loop
root.mainloop()