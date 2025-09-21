class Student:
    college_name = "ROOKIESWORLD"
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        return f"Name: {self.name} Marks: {self.marks}"
    
    @classmethod
    def change_college(self, new_college_name):
        self.college_name = new_college_name
    
    @staticmethod
    def is_adult(age):
        return age > 18
        

s1 = Student("Adam", "99.99")
Student.change_college("Pramod INstitution")
print(Student.is_adult(12))
