#while not excute some code while some condition remain true

food = input("enter the food you like")
while not food == "q":
    print(f"so you like {food}")
    food = input("enter another food you like")
print("nice taste, bye")    