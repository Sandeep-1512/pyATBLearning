## User input: year
## year divisible by 4 but not less than 100

Year = int(input("Enter the year you want to check \n"))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print("Mentioned year is LEAP_Year", Year)
else:
    print("Mentioned Year is  not Leap_Year", Year)
