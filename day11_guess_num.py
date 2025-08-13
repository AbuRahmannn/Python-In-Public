import random

low = 1
high = 6
guess = 0
running = True

number = random.randint(low,high)
answer = number
num = True

print("------------------------------------------------")
print("welcome welcome guess a dice number and win $100")
print("------------------------------------------------")

while num:
    n = input("guess a number between 0 and 6: ")
    if n.isdigit():
        n = int(n)
        guess +=1

        if n > high or n < low:
            print("the number is out of range!!!") 
        elif answer > n:
            print("thats too low, try again")
        elif answer < n:
            print("thats too high, try again")
        else:
                print("thats a correct guess you won $100!!!")
                print("-------------------------")
                print(f"your guesses are {guess}")            
                print("-------------------------")
                num == False
    else:
        print("invalid guess")
        print(f"please enter between {low} and {high}")



