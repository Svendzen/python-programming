class Person:
    """
    A base class for representing a person.
    """
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def get_info(self):
        """
        Prints the full name and age of the person.
        """
        print("Full Name:", self.fname, self.lname)
        print("Age:", self.age)


class Student(Person):
    """
     A class for representing a student, inheriting from Person.
    """
    def __init__(self, fname, lname, age, student_id):
        Person.__init__(self, fname, lname, age)
        self.student_id = student_id

    def get_stuinfo(self):
        """
        Prints the full name, age and student ID of the student.
        """
        self.get_info()
        print("Student ID:", self.student_id)


class Employee(Person):
    """
    A class for representing an employee, inheriting from Person.
    """
    def __init__(self, fname, lname, age, employee_no, salary):
        Person.__init__(self, fname, lname, age)
        self.employee_no = employee_no
        self.salary = salary

    def get_empinfo(self):
        """
        Prints the full name, age, employee number and salary of the employee.
        """
        self.get_info()
        print("Employee No:", self.employee_no)
        print("Salary:", self.salary, "USD")


# Example usage:
new_student = Student("Anthony", "Smith", 35, "s346571")
new_student.get_stuinfo()
print("============================")
new_employee = Employee("Sarah", "Tayolr", 34, 2919736, 5000)
new_employee.get_empinfo()
