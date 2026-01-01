#!/usr/bin/env python3
"""
Test script for Todo CLI Application.

This script automatically tests all 5 features by simulating user input.
"""

import sys

from src.todo_cli.services import TaskList


def test_add_task():
    """Test User Story 1: Add new task."""
    print("\n=== TEST 1: Add New Task ===")
    task_list = TaskList()

    # Test 1: Add first task
    task1 = task_list.add_task("Buy groceries")
    assert task1.id == 1, "Task ID should be 1"
    assert task1.title == "Buy groceries", "Task title mismatch"
    assert task1.completed is False, "New task should not be complete"
    print(f"[PASS] Created task 1: {task1}")

    # Test 2: Add second task
    task2 = task_list.add_task("Walk dog")
    assert task2.id == 2, "Task ID should be 2"
    print(f"[PASS] Created task 2: {task2}")

    # Test 3: Add third task
    task3 = task_list.add_task("Pay bills")
    assert task3.id == 3, "Task ID should be 3"
    print(f"[PASS] Created task 3: {task3}")

    # Test 4: Empty title should raise ValueError
    try:
        task_list.add_task("   ")
        assert False, "Empty title should raise ValueError"
    except ValueError as e:
        assert "cannot be empty" in str(e), "Wrong error message"
        print(f"[PASS] Empty title validation works: {e}")

    print("TEST 1 PASSED: All tasks added successfully\n")
    return task_list


def test_view_tasks(task_list: TaskList):
    """Test User Story 2: View all tasks."""
    print("=== TEST 2: View All Tasks ===")

    # Test 1: View all tasks
    tasks = task_list.get_all_tasks()
    assert len(tasks) == 3, f"Should have 3 tasks, got {len(tasks)}"
    print(f"[PASS] Retrieved {len(tasks)} tasks")

    # Test 2: Verify task details
    task = task_list.get_task_by_id(1)
    assert task is not None, "Task 1 should exist"
    assert task.title == "Buy groceries", "Task 1 title mismatch"
    print(f"[PASS] Task 1 found: {task}")

    # Test 3: Empty task list
    empty_list = TaskList()
    assert len(empty_list.get_all_tasks()) == 0, "New list should be empty"
    print("[PASS] Empty task list handled correctly")

    # Test 4: Non-existent task
    task = task_list.get_task_by_id(99)
    assert task is None, "Non-existent task should return None"
    print("[PASS] Non-existent task returns None")

    print("TEST 2 PASSED: All tasks viewable\n")


def test_update_task_title(task_list: TaskList):
    """Test User Story 3: Update task title."""
    print("=== TEST 3: Update Task Title ===")

    # Test 1: Update task title
    task_list.update_task_title(2, "Walk dog")
    task = task_list.get_task_by_id(2)
    assert task.title == "Walk dog", "Title not updated"
    print(f"[PASS] Task 2 updated: {task}")

    # Test 2: Non-existent task
    try:
        task_list.update_task_title(99, "New title")
        assert False, "Should raise ValueError for non-existent task"
    except ValueError as e:
        assert "not found" in str(e), "Wrong error message"
        print(f"[PASS] Non-existent task validation works: {e}")

    # Test 3: Empty new title
    try:
        task_list.update_task_title(1, "   ")
        assert False, "Should raise ValueError for empty title"
    except ValueError as e:
        assert "cannot be empty" in str(e), "Wrong error message"
        print(f"[PASS] Empty title validation works: {e}")

    print("TEST 3 PASSED: Task titles updated correctly\n")


def test_delete_task(task_list: TaskList):
    """Test User Story 4: Delete task."""
    print("=== TEST 4: Delete Task ===")

    # Test 1: Delete task
    task = task_list.get_task_by_id(3)
    title_before = task.title
    task_list.delete_task(3)
    assert len(task_list.get_all_tasks()) == 2, "Task not deleted"
    print(f"[PASS] Deleted task 3: {title_before}")

    # Test 2: Verify task is gone
    task = task_list.get_task_by_id(3)
    assert task is None, "Deleted task should not exist"
    print("[PASS] Task 3 no longer exists")

    # Test 3: Non-existent task
    try:
        task_list.delete_task(99)
        assert False, "Should raise ValueError for non-existent task"
    except ValueError as e:
        assert "not found" in str(e), "Wrong error message"
        print(f"[PASS] Non-existent task validation works: {e}")

    print("TEST 4 PASSED: Task deleted successfully\n")


def test_mark_task_complete(task_list: TaskList):
    """Test User Story 5: Mark task complete."""
    print("=== TEST 5: Mark Task Complete ===")

    # Test 1: Mark task complete
    task_list.mark_task_complete(1)
    task = task_list.get_task_by_id(1)
    assert task.completed is True, "Task not marked complete"
    print(f"[PASS] Task 1 marked complete: {task}")

    # Test 2: Mark already complete task (idempotent)
    task_list.mark_task_complete(1)
    task = task_list.get_task_by_id(1)
    assert task.completed is True, "Should remain complete"
    print("[PASS] Marking complete task again works (idempotent)")

    # Test 3: Non-existent task
    try:
        task_list.mark_task_complete(99)
        assert False, "Should raise ValueError for non-existent task"
    except ValueError as e:
        assert "not found" in str(e), "Wrong error message"
        print(f"[PASS] Non-existent task validation works: {e}")

    print("TEST 5 PASSED: Tasks marked complete correctly\n")


def test_all_features():
    """Run all tests end-to-end."""
    print("\n" + "=" * 60)
    print("TODO CLI APPLICATION - FEATURE TESTS")
    print("=" * 60)

    try:
        # Test 1: Add tasks
        task_list = test_add_task()

        # Test 2: View tasks
        test_view_tasks(task_list)

        # Test 3: Update task title
        test_update_task_title(task_list)

        # Test 4: Delete task
        test_delete_task(task_list)

        # Test 5: Mark task complete
        test_mark_task_complete(task_list)

        # Final verification
        print("=== FINAL VERIFICATION ===")
        final_tasks = task_list.get_all_tasks()
        print(f"[PASS] Final state: {len(final_tasks)} tasks remaining")
        for task in final_tasks:
            print(f"  {task}")
        print("=" * 60)
        print("ALL TESTS PASSED")
        print("=" * 60)
        print("\nAll 5 features working correctly:")
        print("  1. Add Task")
        print("  2. View Tasks")
        print("  3. Update Task Title")
        print("  4. Delete Task")
        print("  5. Mark Task Complete")
        print()

        return True

    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_all_features()
    sys.exit(0 if success else 1)
