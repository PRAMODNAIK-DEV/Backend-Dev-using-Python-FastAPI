# 🐍 Object-Oriented Programming (OOP) in Python
Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects and classes. It is one of the most widely used approaches in Python due to its ability to create reusable and modular code.

### Key Concepts of OOP:
OOP in Python revolves around four main principles:
1. Class & Object
2. Encapsulation
3. Inheritance
4. Polymorphism
5. Abstraction

---

## 1. Classes and Objects
**Class**: A `class` is a **blueprint** for creating `objects`. It defines attributes (variables) and behaviors (methods) that objects of the class will have.

**Object**: An `object` is an **instance** of a `class`. Each object can have its own data while sharing the same structure (class).


**Example**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Car: {self.brand}, Model: {self.model}")

# Creating objects
car1 = Car("Toyota", "Fortuner")
car2 = Car("Mahindra", "XUV700")

car1.display()
car2.display()
```

Output:
```
Car: Toyota, Model: Fortuner
Car: Mahindra, Model: XUV700
```

---

## 2. `__init__` Constructor
- Special method in Python classes.
- Automatically called when an object is created.

```python
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

s1 = Student("Pramod", 101)
print(s1.name, s1.roll_no)
```
Output:
```
Pramod 101
```

---

## 3. Inheritance
Inheritance allows a class (child) to use methods/attributes of another class (parent).

### Single Inheritance
```python
class Animal:
    def speak(self):
        print("This is an animal.")

class Dog(Animal):
    def bark(self):
        print("Dog barks!")

d = Dog()
d.speak()
d.bark()
```
Output:
```
This is an animal.
Dog barks!
```

### Multiple Inheritance
```python
class Father:
    def skill(self):
        print("Father's skill: Farming")

class Mother:
    def skill(self):
        print("Mother's skill: Cooking")

class Child(Father, Mother):
    def talent(self):
        print("Child's talent: Coding")

c = Child()
c.skill()   # Resolves using Method Resolution Order (MRO)
c.talent()
```
Output:
```
Father's skill: Farming
Child's talent: Coding
```

### Multilevel Inheritance
```python
class Grandparent:
    def say(self):
        print("I am the grandparent.")

class Parent(Grandparent):
    def say(self):
        print("I am the parent.")

class Child(Parent):
    pass

c = Child()
c.say()
```
Output:
```
I am the parent.
```

---

## 4. Encapsulation
- Binding data and methods into a single unit (class).  
- Achieved using private/protected/public access modifiers.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())

# print(acc.__balance)  # Error: Private variable
```
Output:
```
1500
```

---

## 5. Polymorphism
- Same function name but different implementations.

### Function Overloading (Not directly supported, use default args)
```python
class Math:
    def add(self, a=0, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(2, 3))      # 5
print(m.add(2, 3, 4))   # 9
```

### Function Overriding
```python
class Bird:
    def sound(self):
        print("Some generic sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot says: Hello!")

p = Parrot()
p.sound()
```
Output:
```
Parrot says: Hello!
```

---

## 6. Abstraction
- Hiding implementation details, showing only essential features.  
- Achieved using **abstract classes** in Python.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print("Area of circle:", c.area())
```
Output:
```
Area of circle: 78.5
```

---

## 7. Method Resolution Order (MRO)
Defines the order in which Python looks for methods in classes during inheritance.

```python
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.show()
print(D.mro())
```
Output:
```
Class B
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

---

## 8. Static and Class Methods
- **Instance method** → works with `self`  
- **Class method** → works with `cls`  
- **Static method** → doesn’t depend on `self` or `cls`

```python
class Employee:
    company = "ABC Pvt Ltd"

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee:", self.name)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def info():
        print("This is Employee class.")

e1 = Employee("Pramod")
e1.show()
Employee.change_company("XYZ Pvt Ltd")
print(Employee.company)
Employee.info()
```
Output:
```
Employee: Pramod
XYZ Pvt Ltd
This is Employee class.
```

---

## 9. Magic (Dunder) Methods
Special methods starting with `__` and ending with `__`.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)

b = Book("Python Mastery", "Pramod")
print(b)          # Calls __str__
print(len(b))     # Calls __len__
```
Output:
```
Python Mastery by Pramod
14
```

---

# Summary
- **Class & Object** → Blueprint & instance  
- **Constructor (`__init__`)** → Initialize objects  
- **Inheritance** → Reuse code  
- **Encapsulation** → Data hiding  
- **Polymorphism** → Many forms (overloading/overriding)  
- **Abstraction** → Hiding details  
- **MRO** → Resolves method order  
- **Static/Class Methods** → Different method types  
- **Magic Methods** → Built-in operator overloading  

---

✅ With these concepts, students will be ready to apply OOP in **FastAPI projects** effectively.
