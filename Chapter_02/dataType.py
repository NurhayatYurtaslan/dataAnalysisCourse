import numpy as np

ar = np.array([3, 4, 5, 6, 7, 8], dtype=np.int32)
print(ar)
print(ar.dtype)

ar = np.array([3, 4, 5, 6, 7, 8], dtype='f')
print(ar)
print(ar.dtype)

ar = np.array([True, False, False, True], dtype=np.bool_)
print(ar)
print(ar.dtype)

ar = np.array(['kjdsjdskj', 'dsdsd', 'dsdsew'], dtype=np.str_)
print(ar)
print(ar.dtype)

ar = np.array(['k', 'd', 'w'], dtype='S1')
print(ar)
print(ar.dtype)

ar=np.array([1+3j,3+6j,6+3j],dtype=np.complex64)
print(ar)
print(ar.dtype)
