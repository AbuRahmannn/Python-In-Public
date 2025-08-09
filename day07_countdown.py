import time

my_time = int (input("enter the time in second"))
for x in range(my_time , 0 ,-1):
    second = x % 60
    print(f"00:00:{second}")
    time.sleep(1)
print("times up")       