class Student:
    """
    Represents a student with a name and mark, capable of determining if
    the student has passed or failed based on a static passing mark.
    """
    passing_mark = 50  # The shared attribute indicating the mark needed to pass

    def __init__(self, name, mark):
        self.name = name
        self.__mark = mark  # private attribute mark to avoid misuse of sensitive data

    def __str__(self):
        """
        Returns a string representation of the student.
        """
        return f'{self.name} {self.__mark}'

    def get_mark(self):
        """
        Retrieves the mark of the student.
        """
        return self.__mark

    def pass_or_fail(self):
        """
        Returns True or False if the student has passed or failed depending on
        if their mark is higher or equal to the passing mark.
        """
        if self.get_mark() >= Student.passing_mark:
            return "Pass"
        else:
            return "Fail"


# Example usage, with 50 as the passing mark
student1 = Student("John", 52)
status1 = student1.pass_or_fail()
print(status1)
student2 = Student("Jenny", 69)
status2 = student2.pass_or_fail()
print(status2)

Student.passing_mark = 60  # passing mark is now 60 for all student objects
print("")  # new line

# Example usage, with 60 as the passing mark
student1 = Student("John", 52)
status1 = student1.pass_or_fail()
print(status1)
student2 = Student("Jenny", 69)
status2 = student2.pass_or_fail()
print(status2)
