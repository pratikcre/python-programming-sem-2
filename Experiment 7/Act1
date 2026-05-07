# -*- Calculate grade of students -*-
"""
Created on Tue Apr 21 05:21:52 2026

@author: Shahuraj
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("\nStudent Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


# User Input
name = input("Enter student name: ")
marks = float(input("Enter marks: "))

# Create object
s = Student(name, marks)

# Display result
s.display()
