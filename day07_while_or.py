#while not operator

num = int(input("enter a number between 0 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("enter a number between 0 and 10: "))

print(f"your number is{num}")    
