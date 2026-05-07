# -*- calculate salary and bonus -*-
"""
Created on Tue Apr 21 05:18:01 2026

@author: Shahuraj
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self, bonus_percent):
        return (self.salary * bonus_percent) / 100

    def total_salary(self, bonus_percent):
        return self.salary + self.calculate_bonus(bonus_percent)

    def display(self, bonus_percent):
        print("\nEmployee Name:", self.name)
        print("Basic Salary:", self.salary)
        print("Bonus:", self.calculate_bonus(bonus_percent))
        print("Total Salary:", self.total_salary(bonus_percent))


# User Input
name = input("Enter employee name: ")
salary = float(input("Enter salary: "))
bonus_percent = float(input("Enter bonus percentage: "))

# Create object
emp = Employee(name, salary)

# Display result
emp.display(bonus_percent)
