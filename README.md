# Personal Task Manager with Pomodoro Timer 📝🍅

A creative Python GUI project for managing tasks and boosting productivity using the Pomodoro Technique.

## Project Overview

This is a comprehensive task management application with an integrated Pomodoro timer, designed for students and professionals who want to stay organized and productive. The project demonstrates fundamental Python programming concepts suitable for 1st year B.Tech CSE students.

## Features

### Task Management
- ✅ **Add Tasks**: Easily add new tasks with timestamps
- ✅ **Complete Tasks**: Mark tasks as completed with celebration feedback
- ✅ **Delete Tasks**: Remove tasks you no longer need
- ✅ **Persistent Storage**: All tasks are automatically saved to a JSON file
- ✅ **Task Statistics**: View completion rates and progress

### Pomodoro Timer
- 🍅 **25-Minute Focus Sessions**: Standard Pomodoro work interval
- ☕ **5-Minute Breaks**: Automated break periods after each session
- ⏸️ **Pause/Resume**: Flexible timer control
- 🔄 **Reset**: Start fresh anytime
- 🔔 **Notifications**: Get alerts when sessions complete

### User Interface
- 🎨 **Clean GUI**: Built with Tkinter for a professional look
- 📊 **Real-time Statistics**: Track your productivity
- 🖥️ **Responsive Design**: Resizable window with organized layout
- 🎯 **User-friendly**: Intuitive controls and clear feedback

## Technologies Used

- **Python 3.x**: Core programming language
- **Tkinter**: GUI framework (built-in with Python)
- **JSON**: Data persistence
- **Threading**: For non-blocking timer functionality
- **datetime**: Time and date handling

## Installation

### Prerequisites
- Python 3.6 or higher installed on your system
- Tkinter (usually comes pre-installed with Python)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/debayan888/CS-Project.git
   cd CS-Project
   ```

2. **Verify Python installation**
   ```bash
   python --version
   # or
   python3 --version
   ```

3. **Run the application**
   ```bash
   python task_manager.py
   # or
   python3 task_manager.py
   ```

## Usage Guide

### Getting Started

1. **Launch the Application**
   - Run `python task_manager.py`
   - The main window will appear with task management and timer sections

2. **Adding Tasks**
   - Type your task in the "Task" input field
   - Click "Add Task" or press Enter
   - Your task will appear in the task list

3. **Managing Tasks**
   - **Complete**: Select a task and click "✓ Complete" to mark it done
   - **Delete**: Select a task and click "🗑 Delete" to remove it
   - **Refresh**: Click "🔄 Refresh" to update the display

4. **Using the Pomodoro Timer**
   - Click "▶ Start" to begin a 25-minute focus session
   - Use "⏸ Pause" to temporarily stop the timer
   - Click "⏹ Reset" to start over
   - After 25 minutes, you'll get a notification to take a 5-minute break

### Tips for Maximum Productivity

- 🎯 Start your day by adding all your tasks
- 🍅 Use one Pomodoro session per task
- ☕ Take breaks seriously - they help you stay fresh
- 📊 Check your statistics to track progress
- ✅ Complete tasks to see your productivity grow

## Project Structure

```
CS-Project/
│
├── task_manager.py      # Main application file
├── tasks_data.json      # Auto-generated data file (created on first run)
├── README.md            # This file
└── requirements.txt     # Python dependencies (optional)
```

## Key Programming Concepts Demonstrated

This project showcases several important concepts for CSE students:

1. **Object-Oriented Programming (OOP)**
   - Class-based architecture
   - Encapsulation of data and methods
   - Constructor and instance methods

2. **GUI Programming**
   - Tkinter widgets and layout management
   - Event handling and callbacks
   - Thread-safe GUI updates

3. **File I/O Operations**
   - Reading and writing JSON files
   - Data persistence
   - Error handling

4. **Data Structures**
   - Lists and dictionaries
   - JSON data manipulation
   - CRUD operations (Create, Read, Update, Delete)

5. **Multithreading**
   - Non-blocking timer implementation
   - Daemon threads
   - Thread-safe operations

6. **Date and Time Handling**
   - datetime module usage
   - Time formatting
   - Timer countdown logic

## Customization Options

You can easily customize the timer durations by modifying these variables in `task_manager.py`:

```python
self.pomodoro_duration = 25 * 60  # Change 25 to desired minutes
self.break_duration = 5 * 60      # Change 5 to desired break minutes
```

## Data Storage

- Tasks are stored in `tasks_data.json`
- The file is automatically created on first run
- Data persists between application sessions
- Backup your JSON file to preserve your data

## Troubleshooting

### Application won't start
- Ensure Python 3.x is installed: `python --version`
- Check if Tkinter is available: `python -c "import tkinter"`
- On Linux, install tkinter: `sudo apt-get install python3-tk`

### Tasks not saving
- Check file permissions in the application directory
- Ensure you have write access to create `tasks_data.json`

### Timer not working
- The timer runs in a separate thread
- If paused, click "Start" to resume
- Use "Reset" if the timer seems stuck

## Future Enhancements

Potential features for expansion:
- Task categories and tags
- Task priority levels
- Custom timer durations
- Dark mode theme
- Task search and filter
- Export tasks to CSV
- Sound notifications
- Statistics graphs

## Learning Outcomes

By studying and modifying this project, students will learn:
- How to build desktop applications with Python
- GUI design principles and best practices
- Data persistence techniques
- Time management application logic
- Thread programming basics
- User experience design

## Contributing

This is an educational project for VITIYARTHI certification. Feel free to:
- Fork the repository
- Experiment with new features
- Customize the design
- Share improvements

## License

This project is created for educational purposes as part of CSE coursework.

## Author

Created as part of B.Tech CSE curriculum project for VITIYARTHI certification.

## Acknowledgments

- Inspired by the Pomodoro Technique® by Francesco Cirillo
- Built for students learning Python programming
- Designed to be simple yet functional

---

**Happy Coding and Stay Productive! 🚀**
