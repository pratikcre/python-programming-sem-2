# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:06:53 2026

@author: User
"""


def calculate_emi(loan_amount, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12
    emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return emi

loan = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = int(input("Enter loan tenure (years): "))

emi = calculate_emi(loan, rate, time)

print(f"\nYour Monthly EMI is: {emi:.2f}")
