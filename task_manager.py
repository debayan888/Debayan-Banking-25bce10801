"""
Personal Task Manager with Pomodoro Timer
A simple GUI application for managing tasks and staying productive
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime
import time
import threading

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager with Pomodoro Timer")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Data file path
        self.data_file = "tasks_data.json"
        
        # Load tasks
        self.tasks = self.load_tasks()
        
        # Pomodoro timer variables
        self.timer_running = False
        self.timer_seconds = 0
        self.pomodoro_duration = 25 * 60  # 25 minutes in seconds
        self.break_duration = 5 * 60  # 5 minutes in seconds
        self.is_break = False
        
        # Create UI
        self.create_ui()
        
        # Update task list
        self.refresh_task_list()
    
    def create_ui(self):
        """Create the user interface"""
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="📝 Personal Task Manager", 
                               font=("Arial", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Task Input Frame
        input_frame = ttk.LabelFrame(main_frame, text="Add New Task", padding="10")
        input_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)
        
        ttk.Label(input_frame, text="Task:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.task_entry = ttk.Entry(input_frame, width=40)
        self.task_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        
        ttk.Button(input_frame, text="Add Task", command=self.add_task).grid(
            row=0, column=2, padx=5)
        
        # Task List Frame
        list_frame = ttk.LabelFrame(main_frame, text="Tasks", padding="10")
        list_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        # Task listbox with scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        self.task_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set,
                                       font=("Arial", 10), height=15)
        self.task_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.config(command=self.task_listbox.yview)
        
        # Task action buttons
        button_frame = ttk.Frame(list_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0))
        
        ttk.Button(button_frame, text="✓ Complete", command=self.complete_task).pack(
            side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="🗑 Delete", command=self.delete_task).pack(
            side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="🔄 Refresh", command=self.refresh_task_list).pack(
            side=tk.LEFT, padx=5)
        
        # Pomodoro Timer Frame
        timer_frame = ttk.LabelFrame(main_frame, text="🍅 Pomodoro Timer", padding="10")
        timer_frame.grid(row=2, column=1, sticky=(tk.W, tk.E, tk.N), padx=(10, 0))
        
        self.timer_label = ttk.Label(timer_frame, text="25:00", 
                                     font=("Arial", 32, "bold"))
        self.timer_label.pack(pady=10)
        
        self.timer_status_label = ttk.Label(timer_frame, text="Ready to focus", 
                                           font=("Arial", 10))
        self.timer_status_label.pack(pady=5)
        
        timer_button_frame = ttk.Frame(timer_frame)
        timer_button_frame.pack(pady=10)
        
        self.start_button = ttk.Button(timer_button_frame, text="▶ Start", 
                                       command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.pause_button = ttk.Button(timer_button_frame, text="⏸ Pause", 
                                       command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(timer_button_frame, text="⏹ Reset", 
                  command=self.reset_timer).pack(side=tk.LEFT, padx=5)
        
        # Statistics Frame
        stats_frame = ttk.LabelFrame(timer_frame, text="Statistics", padding="10")
        stats_frame.pack(pady=10, fill=tk.X)
        
        self.stats_label = ttk.Label(stats_frame, text=self.get_statistics(), 
                                     font=("Arial", 9))
        self.stats_label.pack()
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return {"tasks": [], "completed": 0, "total": 0}
        return {"tasks": [], "completed": 0, "total": 0}
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f, indent=4)
    
    def add_task(self):
        """Add a new task"""
        task_text = self.task_entry.get().strip()
        if task_text:
            task = {
                "id": len(self.tasks["tasks"]) + 1,
                "text": task_text,
                "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "completed": False
            }
            self.tasks["tasks"].append(task)
            self.tasks["total"] += 1
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
            self.refresh_task_list()
            messagebox.showinfo("Success", "Task added successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter a task description!")
    
    def complete_task(self):
        """Mark selected task as completed"""
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            # Get only pending tasks
            pending_tasks = [t for t in self.tasks["tasks"] if not t["completed"]]
            if index < len(pending_tasks):
                task_id = pending_tasks[index]["id"]
                # Find and mark task as completed
                for task in self.tasks["tasks"]:
                    if task["id"] == task_id:
                        task["completed"] = True
                        task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        break
                self.tasks["completed"] += 1
                self.save_tasks()
                self.refresh_task_list()
                messagebox.showinfo("Success", "Task marked as completed! 🎉")
        else:
            messagebox.showwarning("Warning", "Please select a task to complete!")
    
    def delete_task(self):
        """Delete selected task"""
        selection = self.task_listbox.curselection()
        if selection:
            if messagebox.askyesno("Confirm", "Are you sure you want to delete this task?"):
                index = selection[0]
                pending_tasks = [t for t in self.tasks["tasks"] if not t["completed"]]
                if index < len(pending_tasks):
                    task_id = pending_tasks[index]["id"]
                    self.tasks["tasks"] = [t for t in self.tasks["tasks"] if t["id"] != task_id]
                    self.tasks["total"] -= 1
                    self.save_tasks()
                    self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")
    
    def refresh_task_list(self):
        """Refresh the task list display"""
        self.task_listbox.delete(0, tk.END)
        pending_tasks = [t for t in self.tasks["tasks"] if not t["completed"]]
        
        if not pending_tasks:
            self.task_listbox.insert(tk.END, "No pending tasks! Add a new task to get started.")
        else:
            for task in pending_tasks:
                display_text = f"• {task['text']} (Added: {task['created'].split()[0]})"
                self.task_listbox.insert(tk.END, display_text)
        
        # Update statistics
        self.stats_label.config(text=self.get_statistics())
    
    def get_statistics(self):
        """Get task statistics"""
        total = self.tasks["total"]
        completed = self.tasks["completed"]
        pending = len([t for t in self.tasks["tasks"] if not t["completed"]])
        
        if total > 0:
            completion_rate = (completed / total) * 100
            return f"Total: {total} | Completed: {completed} | Pending: {pending}\nCompletion Rate: {completion_rate:.1f}%"
        return "Total: 0 | Completed: 0 | Pending: 0\nCompletion Rate: 0%"
    
    def start_timer(self):
        """Start the Pomodoro timer"""
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            
            if self.timer_seconds == 0:
                self.timer_seconds = self.pomodoro_duration if not self.is_break else self.break_duration
                self.timer_status_label.config(
                    text="Focus time! 🎯" if not self.is_break else "Break time! ☕"
                )
            
            # Start timer in separate thread
            threading.Thread(target=self.run_timer, daemon=True).start()
    
    def pause_timer(self):
        """Pause the Pomodoro timer"""
        self.timer_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.timer_status_label.config(text="Paused ⏸")
    
    def reset_timer(self):
        """Reset the Pomodoro timer"""
        self.timer_running = False
        self.timer_seconds = 0
        self.is_break = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.timer_label.config(text="25:00")
        self.timer_status_label.config(text="Ready to focus")
    
    def run_timer(self):
        """Run the timer countdown"""
        while self.timer_running and self.timer_seconds > 0:
            time.sleep(1)
            if self.timer_running:
                self.timer_seconds -= 1
                minutes = self.timer_seconds // 60
                seconds = self.timer_seconds % 60
                self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        
        if self.timer_seconds == 0 and self.timer_running:
            self.timer_complete()
    
    def timer_complete(self):
        """Handle timer completion"""
        self.timer_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        
        if not self.is_break:
            messagebox.showinfo("Pomodoro Complete!", 
                              "Great work! Time for a break! 🎉")
            self.is_break = True
            self.timer_seconds = self.break_duration
            self.timer_label.config(text=f"{self.break_duration // 60:02d}:00")
            self.timer_status_label.config(text="Ready for break")
        else:
            messagebox.showinfo("Break Complete!", 
                              "Break's over! Ready to focus again? 💪")
            self.is_break = False
            self.timer_seconds = self.pomodoro_duration
            self.timer_label.config(text="25:00")
            self.timer_status_label.config(text="Ready to focus")

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
