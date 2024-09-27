import numpy as np

a = np.array([1,2,3,4,5])

print(a)
print(type(a))
print(a[1])
print(a[1:])


a_mul = np.array([[[1,2,3,1],
                   [4,5,6,1],
                   [7,8,9,1]],         
                  [[1,1,1,1],
                   [1,1,1,1],
                   [1,1,1,1]]])

print(a_mul[0])
print(a_mul[0,1])
print(a_mul.shape)
print(a_mul.ndim)
print(a_mul.size)
print(a_mul.dtype)




ab = np.full((2,3,4), 9)
print(ab)


ab = np.zeros((10,5,2))
print(ab)

ab = np.ones((10,5,2))
print(ab)

ab = np.empty((5,5,5))
print(ab)



x_values = np.arange(0, 1000, 5)
print(x_values)