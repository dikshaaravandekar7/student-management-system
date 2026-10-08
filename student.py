students={}

def add_student(roll,name):
    if roll in students:
        return False
    students[roll] = name
    return True

def remove_student(roll):
    if roll in students:
        del students[roll]
        return True
    return False

def search_student(roll):
    if roll in students:
        return f"Student found: {students[roll]}"
    return "Student not found"

def update_student(roll,new_name):
    if roll in students:
        students[roll] = new_name
        return True
    return False

def export_students():
    return students
