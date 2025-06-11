import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def save_todos(self):
        """Save todos to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_task(self, task):
        """Add a new task"""
        new_task = {
            'id': len(self.todos) + 1,
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.todos.append(new_task)
        self.save_todos()
        print(f"✅ Task added: {task}")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.todos:
            print("📝 No tasks found!")
            return
        
        print("\n📋 Your To-Do List:")
        print("-" * 50)
        
        for todo in self.todos:
            status = "✅" if todo['completed'] else "⭕"
            print(f"{status} [{todo['id']}] {todo['task']}")
            print(f"   Created: {todo['created_at']}")
        print("-" * 50)
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for todo in self.todos:
            if todo['id'] == task_id:
                if todo['completed']:
                    print(f"⚠️  Task {task_id} is already completed!")
                else:
                    todo['completed'] = True
                    todo['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.save_todos()
                    print(f"🎉 Task {task_id} marked as completed!")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def delete_task(self, task_id):
        """Delete a task"""
        for i, todo in enumerate(self.todos):
            if todo['id'] == task_id:
                deleted_task = self.todos.pop(i)
                # Reorder IDs after deletion
                for j, remaining_todo in enumerate(self.todos[i:], start=i):
                    remaining_todo['id'] = j + 1
                self.save_todos()
                print(f"🗑️  Deleted task: {deleted_task['task']}")
                return
        print(f"❌ Task with ID {task_id} not found!")
    
    def clear_completed(self):
        """Remove all completed tasks"""
        completed_count = sum(1 for todo in self.todos if todo['completed'])
        if completed_count == 0:
            print("ℹ️  No completed tasks to clear!")
            return
        
        self.todos = [todo for todo in self.todos if not todo['completed']]
        # Reorder IDs
        for i, todo in enumerate(self.todos):
            todo['id'] = i + 1
        self.save_todos()
        print(f"🧹 Cleared {completed_count} completed task(s)!")
    
    def show_stats(self):
        """Show task statistics"""
        total = len(self.todos)
        completed = sum(1 for todo in self.todos if todo['completed'])
        pending = total - completed
        
        print(f"\n📊 Task Statistics:")
        print(f"Total tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")
        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"Completion rate: {completion_rate:.1f}%")

def main():
    app = TodoApp()
    
    print("🎯 Welcome to Your To-Do List App!")
    print("Type 'help' to see available commands")
    
    while True:
        try:
            command = input("\n> ").strip().lower()
            
            if command == 'help':
                print("\n📖 Available Commands:")
                print("  add <task>     - Add a new task")
                print("  list           - View all tasks")
                print("  complete <id>  - Mark task as completed")
                print("  delete <id>    - Delete a task")
                print("  clear          - Remove all completed tasks")
                print("  stats          - Show task statistics")
                print("  help           - Show this help message")
                print("  quit           - Exit the app")
            
            elif command == 'list':
                app.view_tasks()
            
            elif command.startswith('add '):
                task = command[4:].strip()
                if task:
                    app.add_task(task)
                else:
                    print("❌ Please provide a task description!")
            
            elif command.startswith('complete '):
                try:
                    task_id = int(command[9:].strip())
                    app.complete_task(task_id)
                except ValueError:
                    print("❌ Please provide a valid task ID!")
            
            elif command.startswith('delete '):
                try:
                    task_id = int(command[7:].strip())
                    app.delete_task(task_id)
                except ValueError:
                    print("❌ Please provide a valid task ID!")
            
            elif command == 'clear':
                app.clear_completed()
            
            elif command == 'stats':
                app.show_stats()
            
            elif command in ['quit', 'exit', 'q']:
                print("👋 Goodbye! Stay productive!")
                break
            
            elif command == '':
                continue
            
            else:
                print("❌ Unknown command. Type 'help' for available commands.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Stay productive!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()