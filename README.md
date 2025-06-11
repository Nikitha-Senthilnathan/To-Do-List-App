# 🎯 Python To-Do List App

A simple, intuitive command-line to-do list application built with Python. Keep track of your tasks with persistent storage and a clean, emoji-enhanced interface.

## ✨ Features

- **📝 Add Tasks**: Create new tasks with automatic timestamps
- **📋 View Tasks**: Display all tasks with completion status
- **✅ Complete Tasks**: Mark tasks as done when finished
- **🗑️ Delete Tasks**: Remove individual tasks you no longer need
- **🧹 Clear Completed**: Remove all finished tasks at once
- **📊 Statistics**: View task completion rates and counts
- **💾 Persistent Storage**: Tasks are automatically saved to JSON file
- **🎨 User-Friendly Interface**: Clean command-line interface with emojis

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- No additional packages required (uses only built-in libraries)

### Installation

1. **Clone or download** the `todo_app.py` file
2. **Navigate** to the directory containing the file
3. **Run** the application:

```bash
python todo_app.py
```

## 📖 Usage

### Starting the App

```bash
python todo_app.py
```

You'll see the welcome message and can start entering commands.

### Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add <task>` | Add a new task | `add Buy groceries` |
| `list` | View all tasks | `list` |
| `complete <id>` | Mark task as completed | `complete 1` |
| `delete <id>` | Delete a task | `delete 2` |
| `clear` | Remove all completed tasks | `clear` |
| `stats` | Show task statistics | `stats` |
| `help` | Show available commands | `help` |
| `quit` | Exit the application | `quit` |

### Example Session

```
🎯 Welcome to Your To-Do List App!
Type 'help' to see available commands

> add Buy groceries
✅ Task added: Buy groceries

> add Finish project report
✅ Task added: Finish project report

> list

📋 Your To-Do List:
--------------------------------------------------
⭕ [1] Buy groceries
   Created: 2024-12-01 10:30:15
⭕ [2] Finish project report
   Created: 2024-12-01 10:30:25
--------------------------------------------------

> complete 1
🎉 Task 1 marked as completed!

> stats

📊 Task Statistics:
Total tasks: 2
Completed: 1
Pending: 1
Completion rate: 50.0%

> quit
👋 Goodbye! Stay productive!
```

## 📁 File Structure

```
your-project-folder/
├── todo_app.py      # Main application file
├── todos.json       # Auto-generated data file (created after first use)
└── README.md        # This file
```

## 🔧 Technical Details

### Data Storage

- Tasks are stored in `todos.json` in the same directory as the script
- Each task contains:
  - `id`: Unique identifier
  - `task`: Task description
  - `completed`: Boolean completion status
  - `created_at`: Timestamp when task was created
  - `completed_at`: Timestamp when task was completed (if applicable)

### Task ID Management

- Tasks are automatically assigned sequential IDs
- When tasks are deleted, remaining tasks are renumbered to maintain consecutive IDs
- This ensures you can always reference tasks by their displayed numbers

## 🛠️ Customization

### Changing the Data File Location

You can specify a custom filename when creating the TodoApp instance:

```python
app = TodoApp("my_custom_todos.json")
```

### Adding New Features

The code is structured with clear methods that make it easy to extend:

- `add_task()`: Add new tasks
- `view_tasks()`: Display tasks
- `complete_task()`: Mark tasks complete
- `delete_task()`: Remove tasks
- `clear_completed()`: Bulk remove completed tasks
- `show_stats()`: Display statistics

## 🐛 Troubleshooting

### Common Issues

**"Permission denied" error**
- Make sure you have write permissions in the directory
- Try running from a different location

**"File not found" error**
- The app will create `todos.json` automatically on first use
- Make sure Python has permission to create files in the current directory

**Tasks not saving**
- Check disk space
- Verify file permissions
- Ensure the directory is writable

### Error Handling

The app includes robust error handling for:
- Invalid JSON data
- File permission issues
- Invalid user input
- Keyboard interrupts (Ctrl+C)

## 🤝 Contributing

Feel free to enhance this to-do app! Some ideas for improvements:

- **Due dates**: Add deadline functionality
- **Categories**: Organize tasks by category/project
- **Priority levels**: High, medium, low priority tasks
- **Search**: Find tasks by keyword
- **Export**: Export tasks to different formats
- **GUI version**: Create a graphical interface

## 📄 License

This project is open source. Feel free to use, modify, and distribute as needed.

## 📧 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the example usage
3. Make sure you're using Python 3.6+

---

**Happy task managing! 🎉**
