# calculate EMI based on loan amount, rate, and years
"""
Created on Mon Mar 23 03:30:54 2026

@author: Shahuraj Mane
"""

def calculate_emi(principal, annual_rate, years):
    
    monthly_rate = annual_rate / (12 * 100)
    
    months = years * 12
    
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    
    return emi


p = float(input("Enter loan amount: "))
r = float(input("Enter annual interest rate (%): "))
t = int(input("Enter time (years): "))

emi = calculate_emi(p, r, t)

print(f"Monthly EMI = {emi:.2f}")
