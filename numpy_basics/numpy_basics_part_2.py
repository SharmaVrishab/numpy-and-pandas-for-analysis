import numpy as np

#  creating array with existing data

a = np.arange(1,11)
arr_1 = a[3:8]
print(arr_1)



a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])




#  vertically stack
print(np.vstack((a1,a2)))

#  horizontal stacking
print(np.hstack((a1, a2)))



# we can also do splitting
# horizontal
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8]])
print(np.hsplit(a, 2))

#  vertical split
print(np.vsplit(a, 2))




x = np.arange(1,25).reshape(2,12)
print(x)



#  we can also divide the data into 3 parts using
print(np.hsplit(x,3))


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
cpy_1 = a[0,:]
cpy_1[0] =  99
print(a)

#   how should copying should actually be done
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
cpy_2 = a.copy()
cpy_2[0] =  99
print(a)




#  BASIC ARRAY OPERATIONS

data = np.array([1, 2])
ones = np.ones(2, dtype=int)


print(data+ones)
print(data-ones)
print(data * data)


a = np.array([1,2,3,4,5])
print(a.sum())


#  for sum in 2d array

b = np.array([[1, 0],
              [2, 2]])
print(b.sum(axis=0))
print(b.sum(axis=1))



#  BROADCASTING

data = np.ones(5)
print(data * 4)



#  row wise broadcasting
a = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2, 3)

b = np.array([10, 20, 30])  # shape (3,)

#  actualy b -> 1 row 3 columns so -> 2,3 amd 1,3 the right most columns match


#  column wise broadcasting

a = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2, 3)

c = np.array([[10],
              [20]])   # shape (2, 1)

print(a*c)


data = np.ones(5)
print(data.max())
print(data.min())
print(data.sum())



#  generate random number

rng = np.random.default_rng(42)
print(rng.random(3))
print(rng.random(3))

rng = np.random.default_rng()
print(rng.integers(5, size=(2, 4)))


#  get unique value
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(a)
print(unique_values)
#  return index
unique_values = np.unique(a,return_index=True)
print(unique_values)
print(unique_values[1])

#  return count
unique_values, occurrence_count = np.unique(a, return_counts=True)
print(occurrence_count)



# getting row and column wise unique

#  this flatted our array
a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
print(np.unique(a_2d))

a_2d = np.array(
                 [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [1, 2, 3, 4]
                 ]
                )
print(np.unique(a_2d,axis=0))



#  checking column for uniqueness

a_2d = np.array([
    [1, 2, 3, 2],
    [4, 5, 6, 5],
    [7, 8, 9, 8]
])

print(np.unique(a_2d,axis=1))



#  transposing

data = np.arange(1,22)
data_2d = data.reshape(7,3)
print(data)
print(data_2d.T)


#  reverse a array

a = np.linspace(1,20)
print(np.flip(a))



#  flattening md array
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(x.flatten())

# ravel also do the same thing but the same object to do that ie if you make changes
#  it will affect the original one too
a1 = x.flatten()
a1[0] = 99
print(x)  # Original array
print(a1)  # New array
