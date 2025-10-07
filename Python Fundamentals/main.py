
class Student:
    college = "ROOKIES"
    
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def printDetails(self):
        return f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}, College: {self.college}"

    def printMarks(self):
        return f"Marks: {self.marks}"
    
    @classmethod
    def changeCollege(cls, new_college):
        cls.college = new_college
    
    @staticmethod
    def add(a, b):
        return a + b
    
    
# Instantiation - Creating an Object/Instance
pramod = Student("Pramod", 24, 85)

print(Student.add(2,4))
print(pramod.add(5,6))
