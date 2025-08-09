#nested loop
rows = int(input("enter num of rows"))
cols = int(input("enter num of cols"))
sym = input("enter a symbol")

for x in range(rows):
    for y in range(cols):
        print(sym,end=" ")
    print()