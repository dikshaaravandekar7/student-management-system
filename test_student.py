import pytest
from student import *

def setup_function():
    students.clear()

def test_add_student():
    assert add_student(1,"Alice") == True

def test_duplicate_student():
    add_student(1,"Alice")
    assert add_student(1, "Bob") == False

def test_remove_student():
    add_student(1,"Alice")
    assert remove_student(1) == True

def test_remove_non_existing():
    assert remove_student(2) == False

def test_search_student():
    add_student(1,"Alice")
    assert search_student(1) == "Student found: Alice"

def test_search_non_existing():
    assert search_student(2) == "Student not found"

def test_update_student():
    add_student(1,"Alice")
    assert update_student(1,"Bob") == True

def test_update_non_existing():
    assert update_student(2, "Bob") == False

def test_search_after_update():
    add_student(1,"Alice")
    update_student(1, "Bob")
    assert search_student(1) == "Student found: Bob"

def test_add_multiple_students():
    add_student(1,"Alice")
    add_student(2,"Bob")
    assert len(students) == 2
