# TypeCasting

name = "rahman" #string
null = " "
age = 19 #number
cgpa = 7.55 #float
letter = 69
student = True #boolean

#type() to check the type of the variables
"""
print(type(name))
print(type(age))
print(type(student))
print(type(cgpa))

"""

#to typecast int() str() float() bool()

age = float(age) # int to float()
print(age)
print(type(age))

cgpa = int(cgpa) #float to int()
print(cgpa)
print(type(cgpa))

letter = str(letter)#int to str()
print(letter)
print(type(letter))

clg = "aliet"
collge = ""
clg = bool(clg)  #string to boolean
collge = bool(collge)
print(clg)
print(collge)
print(type(clg))
print(type(collge)) #because of empty "" its False