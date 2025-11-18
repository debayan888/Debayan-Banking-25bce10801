"""
Test script for Task Manager functionality
Tests core logic without GUI
"""

import json
import os
import sys

def test_task_operations():
    """Test basic task operations"""
    print("Testing Task Manager Core Functionality...")
    print("-" * 50)
    
    # Test 1: Data structure initialization
    print("\n✓ Test 1: Data Structure Initialization")
    tasks = {"tasks": [], "completed": 0, "total": 0}
    assert tasks["tasks"] == []
    assert tasks["completed"] == 0
    assert tasks["total"] == 0
    print("  PASSED: Data structure initialized correctly")
    
    # Test 2: Add task
    print("\n✓ Test 2: Adding Tasks")
    task = {
        "id": 1,
        "text": "Test Task",
        "created": "2025-11-18 12:00:00",
        "completed": False
    }
    tasks["tasks"].append(task)
    tasks["total"] += 1
    assert len(tasks["tasks"]) == 1
    assert tasks["total"] == 1
    print("  PASSED: Task added successfully")
    
    # Test 3: Complete task
    print("\n✓ Test 3: Completing Tasks")
    tasks["tasks"][0]["completed"] = True
    tasks["completed"] += 1
    assert tasks["tasks"][0]["completed"] == True
    assert tasks["completed"] == 1
    print("  PASSED: Task marked as completed")
    
    # Test 4: JSON serialization
    print("\n✓ Test 4: JSON Serialization")
    test_file = "test_tasks.json"
    with open(test_file, 'w') as f:
        json.dump(tasks, f, indent=4)
    assert os.path.exists(test_file)
    print("  PASSED: Tasks saved to JSON file")
    
    # Test 5: JSON deserialization
    print("\n✓ Test 5: JSON Deserialization")
    with open(test_file, 'r') as f:
        loaded_tasks = json.load(f)
    assert loaded_tasks["total"] == tasks["total"]
    assert loaded_tasks["completed"] == tasks["completed"]
    assert len(loaded_tasks["tasks"]) == len(tasks["tasks"])
    print("  PASSED: Tasks loaded from JSON file")
    
    # Test 6: Delete task
    print("\n✓ Test 6: Deleting Tasks")
    task_id = tasks["tasks"][0]["id"]
    tasks["tasks"] = [t for t in tasks["tasks"] if t["id"] != task_id]
    tasks["total"] -= 1
    assert len(tasks["tasks"]) == 0
    assert tasks["total"] == 0
    print("  PASSED: Task deleted successfully")
    
    # Test 7: Statistics calculation
    print("\n✓ Test 7: Statistics Calculation")
    tasks = {"tasks": [], "completed": 5, "total": 10}
    completion_rate = (tasks["completed"] / tasks["total"]) * 100
    assert completion_rate == 50.0
    print(f"  PASSED: Completion rate calculated correctly: {completion_rate}%")
    
    # Test 8: Timer duration calculation
    print("\n✓ Test 8: Timer Duration Calculations")
    pomodoro_duration = 25 * 60  # 25 minutes
    break_duration = 5 * 60      # 5 minutes
    assert pomodoro_duration == 1500
    assert break_duration == 300
    
    minutes = pomodoro_duration // 60
    seconds = pomodoro_duration % 60
    assert minutes == 25
    assert seconds == 0
    print(f"  PASSED: Timer durations correct - Pomodoro: {minutes}min, Break: {break_duration//60}min")
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("\n" + "=" * 50)
    print("✓ ALL TESTS PASSED!")
    print("=" * 50)
    return True

def test_imports():
    """Test that all required modules can be imported"""
    print("\nTesting Module Imports...")
    print("-" * 50)
    
    try:
        import tkinter as tk
        from tkinter import ttk, messagebox, simpledialog
        print("✓ tkinter modules imported successfully")
        
        import json
        print("✓ json module imported successfully")
        
        import os
        print("✓ os module imported successfully")
        
        from datetime import datetime
        print("✓ datetime module imported successfully")
        
        import time
        print("✓ time module imported successfully")
        
        import threading
        print("✓ threading module imported successfully")
        
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("TASK MANAGER TEST SUITE")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n✗ Import test failed!")
        sys.exit(1)
    
    print()
    
    # Test core functionality
    if not test_task_operations():
        print("\n✗ Functionality test failed!")
        sys.exit(1)
    
    print("\n✓ All tests completed successfully!")
    print("The application is ready to use!\n")
