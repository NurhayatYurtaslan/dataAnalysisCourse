import numpy as np
ar=np.array([1,4,5,6,7,8],dtype='i')
print("original array",ar)
print("original array data type",ar.dtype)
print("after conversion")
float_ar=ar.astype(np.float64)
print("New float typed array" , float_ar)
print("New array data type",float_ar.dtype)
