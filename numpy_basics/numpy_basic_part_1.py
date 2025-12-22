import numpy as np

# you cannot grow the size of array

a = np.array([1,2,3])


a  = np.append(a,4)


a= np.array(
    [
        [1,2,3],
        [3,4,5]
    ]
)


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a.ndim)
print(a.size)
print(a.dtype)


# practising ndim
a = np.array([1,2,3])
print(a.ndim)
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ])
print(a.ndim)
a = np.array(
    [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ],
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
    ])
print(a.ndim)



# CREATING BASIC ARRAY
#  filling array with zeros
a = np.zeros(2,dtype=int)
print(a)
#  filling array with ones
a = np.ones(2,dtype=int)
print(a)

#  we can also create an empty array with random values
a = np.empty(2)
print(a)


#  creating array with range of values
a = np.arange(10)
print(a)

# range with skip
a = np.arange(0,10,2)
print(a)

#  evenly spaced numbers over a interval

a = np.linspace(1,10,5)
print(a)


#  ADDING , REMOVING AND SORTING ELEMENTS
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])


c = np.concatenate((a,b))
print(c)



# learning about axis

# axis 0
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

print(x.ndim)
print(y.ndim)

c = np.concatenate(
    (x,y)
)

print(c)
print(c.ndim)
print(c.size)
print(c.shape)
# updating b bcz it will give error for above  b due mismatch  dimensions
b = np.array([[5, 6],
              [7, 8]])  # shape (2, 2)


c = np.concatenate(
    (x,b),axis=1
)

print(c)
print(c.ndim)
print(c.size)
print(c.shape)




# RESHAPE ARRAY

a = np.arange(10)
print(a)


b = a.reshape(5,2)
print(b)


#  with order

c = np.reshape(a,shape=(5,2),order='C')
print(c)
c = np.reshape(a,shape=(5,2),order='F')
print(c)



# how to add new axis to element

#  1d to 2d
#  np.newaxis , np.expand_dims


a = np.array([1,2,3,4,5,6])
print(a.shape)


#  adding a new axis

# AXIS 0 -> ROW WISE
# AXIS 1. -> COLUMN WISE

#  this make 1,6

#  when we say adding a axis ie np.newaxis it adds 1 [1,:]
a2 = a[np.newaxis,:]
print(a2)
print(a2.shape)


# this make 6,1 ie 6 rows and 1 columnn
a2 = a[:,np.newaxis]
print(a2)
print(a2.shape)




#  we can also use
c = np.expand_dims(a,axis=1)
print(c)





#  INDEXING AND SLICING


data = np.array([1,2,3])
print(data.shape)

print(data[1])
print(data[1:2])
print(data[1:])
print(data[-2:])



a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


print(a[a<5])

print(a[a>=5])

print(a[a%2==0])


print(a[(a>2) & (a<11)])

print(np.zeros(4))


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# print(np.nonzero(a))

# print(np.where(a!=0))


b = np.nonzero(a < 5)

list_of_coordinates= list(zip(b[0], b[1]))

for coord in list_of_coordinates:
    print(coord)
