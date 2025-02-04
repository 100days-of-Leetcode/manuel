class Student:
    """Just a simple program written for Students"""

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def test_age(self):
        if self.age < 18:
            print(f"{self.age} Too young")

    def test_grade(self):
        if self.grade > 87:
            print(f"{self.grade} too high")
        else:
            print(f"{self.grade} Not bad")



student1 = Student("Harry Potter", 21, 99)
student2 = Student('Maya', 17, 77)
student1.test_age()
student1.test_grade()

