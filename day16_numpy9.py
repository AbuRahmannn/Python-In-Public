import numpy as np
array = np.array([21,17,19,20,16,30,18,65])
                 
# Create random number generator
rnd = np.random.default_rng()

# Roll one dice (1 to 6)
print(rnd.integers(1, 7))  

# Roll three dice
print(rnd.integers(low=1, high=7, size=3))

#floating numbers
print(np.random.uniform(low = -1, high = 1))

print(rnd.shuffle(array))
num = rnd.choice(array)
print(num)