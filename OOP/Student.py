class Student:
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade

    def __str__(self):
        return f"""Name: {self.name}
ID: {self.id}
Grade: {self.grade}"""

    def __lt__(self, other):
        return self.grade < other.grade

    def __eq__(self, other):
        return self.id == other.id

    def GradeType(self):
        if self.grade >= 3.6:
            return 'Excellent'
        elif 3.2 <= self.grade < 3.6:
            return 'Good'
        elif 2.5 <= self.grade < 3.2:
            return 'Fair'
        else:
            return 'Poor'

# Test case:
s1 = Student('Nguyen Van An', 20201000, 3.75)
s2 = Student('Le Van Toan', 20202345, 2.80)
s3 = Student('Tran Thi Dung', 20201000, 3.12)
print(s1)
print(s2 < s1 and s3 < s1)
print(s1 == s3)
print(s1.GradeType())
print(s2.GradeType())