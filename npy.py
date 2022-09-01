import numpy as np

# create an array
data1 = [6, 7.5, 8, 0.21, 1]                # create 1d array
array_d1 = np.array(data1)
print(array_d1)
print(array_d1.shape)
print(len(data1))
print()


data2 = [[1,2,3,4], [5, 6, 7, 8]]           # 2d array
array_d2 = np.array(data2)
print(array_d2)
print(array_d2.shape)
print(array_d2.dtype)
print(array_d2[0][1])                        # extract an element
print(array_d2[[0],[1]])
print(len(data2))
print()


data3 = np.zeros(10,dtype=np.int32)          # 10 0's, default datatype is float
print(data3)                                 # only one num so 1d
print()


data4 = np.ones((3,2),order='C')             # 3 parts and each has 2 elements(col-major)
print(data4)                                 # 2 num so 2d
print()


data5 = np.ones_like(array_d1,dtype=int)     # convert all element to 1
print(data5)
print()


data6 = np.empty((2, 3, 2))                  # 3d with random num
print(data6)                                 # 2 parts with 3 rows 2 cols
print(len(data6))
print()


data7 = array_d1.astype(int)                 # coerce to int
print(data7)
print()
print()
print()




# index/slice/reshape/transpose/stack/ifelse
a = np.arange(6)                           # much quicker than list(range(6))
print(a)
print(a[3])
a[2:4] = '88'
print(a)
print()

b = np.random.randn(2,3,2)                  # normal distribution but cannot define m and sd
c = np.random.rand(6, 3)                    # uniform distri
print(b)
print(c[a > 5])
print(c[~(a > 5),1:])                       # ~ means invert (a<=5)
print(c[a > 5][1:])
print()
print()


d = a.reshape(2,3)                          # reshape
print(d)
print(d[[0,1],[1,2]])
print()
d = a.reshape((2,3,1))                      # two parts each part with 3 row and 1 col
print(d)
print()

e = d.T                                     # transpose
print(e)
print()
print()



f = zip(a, np.array([1,2,6,8]))             # stack 1d array to 2d array
print(np.array(list(f)))
print()
g = np.stack((a,np.array([1,2,6,8,13,15])),axis=0)      # same effect(axis=0 is row, 1 is col)
print(g)
print()
h = np.dstack((a,np.array([1,2,6,8,13,15])))            # stack to 3d array
print(h)
print(h.shape, h.ndim, sep = ' ')
print()
print()



i = np.where(~(a > 3),1,a)
print(i)
print()
print()
print()





# Arithmetic and statistical operations
d1 = np.empty([2,2])
d2 = np.empty([2,2])
print(d1 + d2)
print(d1 - d2)
print(d2 * 2 / 2)
print(d1 // 2)
print(d1 ** 1)
print()

print(np.sqrt(d1))
print(d1.std())
print(np.maximum(d1,d2))
print(d1.sum(axis=1))                           # apply(d1,1,sum) in R but 1 is row 0 is col here differ from top
print(np.any(d1 > 2))                           # any all (same as in R)
print()

print(np.union1d(d1,d2))                        # union two arrays
print(np.in1d(data2,a))                         # check if each element of data2 in a
print()

print(d1.dot(d2))
print(np.dot(d1,np.ones(2)))
print()

