# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

Marks = float(input("Enter your marks"))
if 90 <= Marks <= 100:
    Score = "A"
    print("Your grade is ", Score)
elif 80 <= Marks <= 89:
    Score = "B"
    print("Your grade is ", Score)
elif 70 <= Marks <= 79:
    Score = "C"
    print("Your grade is ", Score)
elif 60 <= Marks <= 69:
    Score = "D"
    print("Your grade is ", Score)
elif Marks >= 100:
    Score = "Outstanding"
    print("You are ", Score)
else:
    Score = "F"
    print("Your grade is ", Score)
