#Filtering with Numpy
import numpy as np
ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,21]])
print("teenage",ages[ages < 18])
print("adults",ages[ages >= 18])
print("seniors",ages[ages >= 65])
print("even",ages[ages%2 == 0])
print("odds",ages[ages%2 != 0])

