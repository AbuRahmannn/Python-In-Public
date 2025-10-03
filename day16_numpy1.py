#multidimentional array with numpy
import numpy as np
array = np.array([[['A','B','C'],['A','B','C'],['A','B','C']],
                   [['A','B','C'],['A','B','C'],['A','B','C']],
                   [['A','B','C'],['A','B','C'],['A','B','C']]])
print(array.ndim)  
print(array.shape)
print(array[0],[0],[0])  #chain indexing               
word = array[0,0,0]+array[0,0,1]
print(word)