#String Methods


#len()
print("using len()")
name = input("enter a name ")
result = len(name)
print(result)

#find a string with first occurance
print("find a string with first occurance")
first = input("enter a string: ")
resu = first.find("a")
print(resu)

#find a string with last occurance
print("find a string with last occurance")
last = input("enter a string: ")
res = last.rfind("a")
print(res)

#make first string letter
print("make first string letter")
capi = input("enter a string")
re = capi.capitalize()
print(re)

#make string upper case
print("making string upper case")
upper = input("enter string to make upper")
r = upper.upper()
print(r)


#make string lower case
print("making string lower case")
lower = input("enter string to make lower")
rr = lower.lower()
print(rr)

#take only digits
digits = input("enter only numbers")
yo = digits.isdigit()
print(yo)

#take only alphabets
alpha = input("enter only alpha")
yoo = alpha.isalpha()
print(yoo)

#count how many times entered
enter = input("enter a string")
yooo = enter.count("-")
print(yooo)

#replace the value in given input
give = input("enter a string")
yepp = give.replace("-","+")
