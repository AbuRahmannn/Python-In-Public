price1 = 3.141559
price2 = 2.2345435
price3 = 6.3345345
price4 = 9.87464535
price5 = 8.67575
price6 = 5.4656456
price7 = 5.4656456
price8 = 55786.4656456
price9 = 56.4656456

print(f"format specific {price1:.2f} ") #only 2f decimals after . point
print(f"format specific {price2:10} ") #give total of 10 digit space
print(f"format specific {price3:010} ") #numbers will br zero 0 padded
print(f"format specific {price4:>10} ") #left justifier
print(f"format specific {price5:<10} ") #right justifier
print(f"format specific {price6:^10} ") #center aligned
print(f"format specific {price6:+} ") #use a + sign
print(f"format specific {price7:-} ") #use a - sign 
print(f"format specific {price8: } ") #use a space seperated with comma
print(f"format specific {price7:,.2f} ")  
