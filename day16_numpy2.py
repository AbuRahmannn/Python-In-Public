#slicing with numpy
import numpy as np
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])
#array[start:end:step]
print(array[1])
print(array[0:3])
print(array[0:4:2])
#column selection
print(array[:,2])