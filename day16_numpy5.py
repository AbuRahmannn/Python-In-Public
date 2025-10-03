#comparision operator in numpy
import numpy as np
scores = np.array([91,55,100,73,82,64])
print(scores == 100)#boolean
scores[scores<60] = 0
print(scores)