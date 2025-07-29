#logical operators
# and, or, not

#using OR logical operator
val = int(input("enter a boolean value"))
if val==0 or val==1:
    print("yes it is boolean")
else:
    print("no its not boolean")    


#using AND logical operator
div = int(input("enter a value which is divisible by 2"))
if div%2==0 and div==0:
    print("it is divisible by 2")
else:
    print("no its not divisible")    


#sing NOT logical operator
b = int(input("enter a value 1"))

if b>0 and not 1:
    print("yes its one or below")
else:
    print("no its not one or below")    
