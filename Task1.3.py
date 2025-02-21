print("""Створити клас Person. Властивості - name. Функції - greet. 
При виклику функції мусить повертатись рядок “Привіт, мене звуть <ім’я>”. 
Створити клас Student, який успадковує Person. 
Функції: is_student -> bool (виведення статусу студента). 
Викликати усі методи для класу Student
""")


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi! My name is {self.name}"


class Student(Person):
    def is_student(self):
        return True


student = Student("Taras")
print(student.greet())
print(student.is_student())
