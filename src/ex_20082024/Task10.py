## Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24
num = int(input("Enter your number: "))
fact = 1
if num == 0 or num ==1:
    fact = 1
    print(1)
else:
    for i in range(1, num+1, 1):
        fact = fact * i

print(fact)
