# Task 1: Check if a Number is Even or Odd
number = int(input("Enter a number: "))
if number%2 ==0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")



# Task 2: sum of numbers from 1 to 50
total = 0
for i in range(1,51,1):
    total = total + i
print(f"total of numbers between 1 and 50 is {total}")
