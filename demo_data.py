"""
Demo script to showcase Task Manager features
Creates sample tasks and demonstrates functionality
"""

import json
import os
from datetime import datetime, timedelta

def create_demo_data():
    """Create sample task data for demonstration"""
    print("Creating demo task data...")
    
    # Sample tasks
    demo_tasks = {
        "tasks": [
            {
                "id": 1,
                "text": "Complete Python assignment on GUI programming",
                "created": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S"),
                "completed": True,
                "completed_at": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
            },
            {
                "id": 2,
                "text": "Study for Data Structures exam",
                "created": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
                "completed": False
            },
            {
                "id": 3,
                "text": "Work on CS project documentation",
                "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "completed": False
            },
            {
                "id": 4,
                "text": "Practice coding problems on LeetCode",
                "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "completed": False
            },
            {
                "id": 5,
                "text": "Attend VITIYARTHI certification workshop",
                "created": (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S"),
                "completed": True,
                "completed_at": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
            }
        ],
        "completed": 2,
        "total": 5
    }
    
    # Save to file
    with open("tasks_data.json", 'w') as f:
        json.dump(demo_tasks, f, indent=4)
    
    print("✓ Demo data created successfully!")
    print(f"\nSample Tasks Created:")
    print("-" * 60)
    
    for task in demo_tasks["tasks"]:
        status = "✓ Completed" if task["completed"] else "○ Pending"
        print(f"{status}: {task['text']}")
    
    print("\n" + "-" * 60)
    print(f"Total Tasks: {demo_tasks['total']}")
    print(f"Completed: {demo_tasks['completed']}")
    print(f"Pending: {demo_tasks['total'] - demo_tasks['completed']}")
    print(f"Completion Rate: {(demo_tasks['completed'] / demo_tasks['total']) * 100:.1f}%")
    print("-" * 60)
    
    print("\n🚀 Now run 'python3 task_manager.py' to see the application!")
    print("   The demo tasks will be loaded automatically.\n")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("TASK MANAGER DEMO - Sample Data Generator")
    print("=" * 60 + "\n")
    
    if os.path.exists("tasks_data.json"):
        response = input("tasks_data.json already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Demo cancelled.")
            exit(0)
    
    create_demo_data()
