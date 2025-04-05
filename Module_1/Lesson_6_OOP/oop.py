# oop.py

class Person:
    def __init__(self, name, age):
        """Initialize a new Person with a name and age."""
        self.name = name
        self.age = age

    def greet(self):
        """Return a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, school):
        """Initialize a new Student with a name, age, and school."""
        super().__init__(name, age)
        self.school = school

    def welcome(self):
        """Return a welcome message specific to the student."""
        return f"Welcome, {self.name} from {self.school}!"


# Testing our classes
if __name__ == "__main__":
    # Create a Person object
    person1 = Person("Alice", 30)
    print(person1.greet())

    # Create a Student object
    student1 = Student("Bob", 20, "Harvard")
    print(student1.greet())
    print(student1.welcome())
