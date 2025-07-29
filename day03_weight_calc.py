#weight calculation using if statements


weight = float(input("enter the weight"))
val = input("choose kilogram or pound(type K or P)")
if val == 'K':
        weight = weight * 2.205
elif unit == 'P'     :
         weight = weight / 2.205
else:
        print("enter valid value")

print(f"the {val} is{weight}")    