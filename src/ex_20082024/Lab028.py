age = int(input("Enter your age : \n"))
if 18 <= age <= 65:
    print("You are allowed to vote ", age)
elif age < 18:
    print("You are minor", age)
else:
    print("You are not allowed", age)
