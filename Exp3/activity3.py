# program for ticket 
"""
Created on Tue Feb 17 11:14:12 2026

@author: pratik mane
"""

rows = 5
cols = 5

seats = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append("O")
    seats.append(row)

while True:
    for i in range(rows):
        for j in range(cols):
            print(seats[i][j], end=" ")
        print()
    
    r = int(input("Enter row number (1-5): ")) - 1
    c = int(input("Enter column number (1-5): ")) - 1
    
    if seats[r][c] == "O":
        seats[r][c] = "X"
        print("Seat booked successfully\n")
    else:
        print("Seat already booked\n")
    
    choice = input("Book another seat? (y/n): ")
    if choice.lower() != "y":
        break
