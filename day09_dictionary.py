#dictionary

capitals = {"usa":"washington", "india":"delhi","japan":"tokyo"}
print(capitals)

print(".get")
capitals.get("india")
print(capitals)

print(".update")
print(capitals.update({"pakistan":"lahore"}))
print(capitals)

print(".pop")
capitals.pop("usa")
print(capitals)

print(".popitem")
capitals.popitem("pakistan") #pop lastest added item
print(capitals)

#capitals.clear

print("print only keys by .keys()")
key = capitals.keys()
print(key)
print(capitals)
#or

'''
key = capitals.keys()
for key in capitals.keys():
    print(key)
'''
print("print only values by .values()")
values = capitals.value()
print(values) #print only values
print(capitals)
#or

'''
for value in capitals.values():
    print(value)
'''

print(".item()")
item = capitals.items()
print(item)
print(capitals)