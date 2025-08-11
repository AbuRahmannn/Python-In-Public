fruits = ["apple","banana","kiwi","coconut"]
veg = ["tomato","potato","carrot"]
meat = ["chicken","mutton","salmon"]
yo = [fruits,veg,meat]
for collection in yo:
    for food in collection:
        print(food, end=" ")
    print( )

