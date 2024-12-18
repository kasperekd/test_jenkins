import pytest
from todo import Task, ToDoList
# tests 2
def test_add_task():
    todo_list = ToDoList()
    todo_list.add_task("Test task")
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].title == "Test task"

def test_remove_task():
    todo_list = ToDoList()
    todo_list.add_task("Task to remove")
    todo_list.remove_task(0)
    assert len(todo_list.tasks) == 0

def test_remove_task_invalid_index():
    todo_list = ToDoList()
    todo_list.add_task("Task")
    todo_list.remove_task(1)
    assert len(todo_list.tasks) == 1

def test_mark_completed():
    todo_list = ToDoList()
    todo_list.add_task("Task to complete")
    todo_list.tasks[0].mark_completed()
    assert todo_list.tasks[0].completed is True
