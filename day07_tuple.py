#tuples  [] 
fruits = ["apple","orange","banana","coconut"]
print(fruits)

print(len(fruits)) #lenght of the tuple

print("apple" in fruits) #boolean value if there yes else no

print(fruits[2]) #to find which value is there at the index

#to change apple to pineapple 
fruits[0] = "pineapple"
print(fruits)

#append = to add
print("append")
print(fruits.append("kiwi"))
print(fruits)


#remove
print("remove")
print(fruits.append("orange"))
print(fruits)

#to insert
print("to insert")
print(fruits.insert(0,"bajji"))

#sort
print("sort")
print(fruits.sort())

#reverse
print("reverse")
print(fruits.reverse())

#clear
print("clear")
print(fruits.clear())


#to find the index of the particular list 
print("finding particular thing's set in the list")
print(fruits.index("coconut"))
