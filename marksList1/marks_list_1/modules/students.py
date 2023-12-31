""" Module to work with students """

from . import marks as mk

ERROR = 1
OK = 0

CHANGE_EXISTS = 1
ADD_NEW_MARK = 2
DELETE_MARK = 3
ADD_NEW_STUDENT = 4
DELETE_STUDENT = 5
SHOW_DB = 6
EXIT_CYCLE = 7


def add_student(cur, con):
    """ Function to add new student to the table"""
    mk.clr_cnsl()
    name = input("Enter student's name:     ")
    if name == "":
        print("Name must be not empty string")
        input()
        return ERROR
    sname = input("Enter student's surname:     ")
    if sname == "":
        print("Surname must be not empty string")
        input()
        return ERROR
    marks = input("Enter student's marks(if he has no marks just push 'Enter')      ")
    if marks.isdigit() or marks == "":
        if mk.check_mark_string(marks):
            print("Marks must be integer numbers")
            return ERROR
    else:
        return ERROR
    cur.execute("""INSERT INTO students (name,surname,marks) VALUES (?,?,?)""", (name,sname,marks))
    con.commit()
    mk.clr_cnsl()
    return OK

def delete_student(cur, con):
    """ Function to delete student from table """

    if mk.check_empty_db(cur):
        print("No students")
        return ERROR
    students = cur.execute(""" SELECT * FROM students """)
    mk.print_db(cur)
    cur.execute(""" SELECT * FROM students """)
    students = cur.fetchall()
    st_id = int(input("Select the id of the student you want to delete:    "))
    if st_id > len(students):
        print("Invalid id")
        input()
        return ERROR
    cur.execute(""" DELETE FROM students WHERE student_id = ? """, (st_id,))
    cur.execute("""UPDATE students SET student_id=student_id - 1 WHERE student_id > ?""", (st_id,))
    con.commit()
    mk.clr_cnsl()
    return OK
