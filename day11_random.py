import random

low = 1
high = 6
options = ("rock","paper","scissor")
print("random int")
number = random.randint(low,high)
print(number)
print("random float")
numbers = random.random()

print(numbers)
print("choice with rock paper scissor")
option = random.choice(options)
print(option)

print("suffle the cards")
uno = ["1","2","3","4","5","6","7","8","9"]
random.shuffle(uno)
print(uno)

