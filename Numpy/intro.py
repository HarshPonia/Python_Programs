"""
Numpy--->   NumPy is a Python library.
            NumPy is used for working with arrays.
            NumPy is short for "Numerical Python".
            NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
"""

# Why is NumPy Faster Than Lists?
#  ----->  NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.


# Demo Ex---> 

import numpy as np
from numpy.core.fromnumeric import ndim
arr = np.array([1,2,3,4,5,6])
print(arr)
print(type(arr))
print(np.__version__)


# 0-D Array using numpy-->

# Ex:-- 
import numpy as np
arr = np.array([11])
print(arr, type(arr), arr.ndim)

# 1-D array using numpy:---->

#An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# These are the most common and basic arrays.
# Ex-->

import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr)
print(type(arr))


# 2-D array using Numpy :-->

# #An array that has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors.

# Ex :-->

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr, type(arr),arr.ndim)


# 3-D Array using Numpy :-->

# Ex:-->

import numpy as np   # we can import numpy as an name
arr = np.array([[1,2],[2,3],[3,4]])
print(arr, type(arr), arr.ndim)



# ndmin in array

# Ex:-->

import numpy as np 
arr = np.array([1,2,3,4,5,6], ndmin = 3)
print(arr,type(arr))


# shape in numpy----> ndarray.shape
# Ex--> 

import numpy as np
d = np.array([[1,2,3],[3,4,5]])
print(d.shape)
print(d)


# Ex 2:--->
import numpy as np
dd = np.array([1,2,3,4,5,6,7,8,9])
dd.shape =3,3
print(dd)
print(dd.shape)


#  >>ndarray.reshape
 
import numpy as np
dd = np.array([1,2,3,4,5,6,7,8,9])
b = dd.reshape(3,3)
print(b)
print(b.shape)


# matrix operation
# matrix multiplication

import numpy as np
matrix1 = np.array([[1,2,3],[3,4,5]])
matrix2 = np.array([[4, 7], [1, 0], [3, 8]])
if matrix1.shape[1] == matrix2.shape[0]:  
    print(np.dot(matrix1,matrix2))   # dot is funtion is used to find the matrix multiplication 
else:
    print("Matrix is not valid")


# element multiplication by using numpy

# Ex :- 

import numpy as np
matrix1 = np.array([[1,2,3],[3,4,5]])
matrix2 = np.array([[4, 7,1], [1, 0,3]])
# matrix2.reshape = 2,2
#print(np.multiply(matrix1, matrix2)) 
print(matrix1.__mul__(matrix2)) # we can also use this mathod to element multiplication


# -->  Type of element in an array in numpy 
# Ex:--->

import numpy as np
m  = np.array([1,3,5,7,13])
print(m)
print(type(m))
print("type of aaray element = ",type(m[0]))   # type of element = <class 'numpy.int32'>


# Type of list  element 

lst = [1,3,5,7,13]
print(type(lst[0]))  #it wiil be simply int type
