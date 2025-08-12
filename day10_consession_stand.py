#program using dictsss
menu = {
    "pizza":3.00,
    "burger":4.00,
    "chips":2.00,
    "soda":2.00,
    "fries":3.00
}
cart = []
total = 0

print("--------MENU-------")
for key,value in menu.items():
    print(f"{key}:${value}")
print("--------------------")    

while True:
    food = input("select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total = total + menu.get(food)
    print(food,end ="")
print()    
print("--------------------")  
print(f"total is:{total:.2f}")
print("--------------------")  