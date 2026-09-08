# to install any module 
# got o terminal and write python -m pip install numpy

# import numpy
import numpy as np

# create a list of sales and convert it to a numpy array
sales = [450,123,1200,765,1230]
arr  = np.array(sales)

print(sales,type(sales))
print(arr,type(arr))

np.array([3,4,5,"hello"])

np.array([3,4,5,9.87])

# 1D array
arr1d = np.array( [3,6,7,4] )
print(arr1d)

arr2d = np.array( [ [5,4,3,2],[9,0,2,5],[1,1,5,4] ]  )
print(arr2d)

arr3d = np.array( [ [[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]] ] )
print(arr3d)

amount = [14, 24, 35, 44, 59]

for i in amount:
    print(i + 100)

arr = np.array([14, 24, 35, 44, 59])

print(arr + 100)

print(arr * 2)

print(arr / 2)

## attributes in numpy

arr = np.array([142, 245, 350, 440, 590])

print(arr)

print(type(arr))

print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr)
print(type(arr))
print(arr.dtype)

# shape of the array

arr = np.array([142, 245, 350, 440, 590])
print(arr)
print(arr.shape)

arr2d = np.array( [ [5,4,3,2],[9,0,2,5],[1,1,5,4] ]  )
print(arr2d)
print(arr2d.shape)

print(arr3d)
print(arr3d.shape)

arr2d

len(arr2d)

# Size of the array

print( arr2d)
print("shape - ", arr2d.shape)
print("size - ", arr2d.size)


# ndim
print("number of dimensions - ", arr.ndim)
print("number of dimensions - ", arr2d.ndim)
print("number of dimensions - ", arr3d.ndim)


## Change data type of an array

arr = np.array([1,2,3,4])
print(arr)
print(arr.dtype)

arr.astype(float)

arr.astype(str)

np.array(["hello how are you good "])

arr = np.array([1.453, 2.345, 3.567,8.9665,12.765])
print(arr)

arr = arr.astype(int)
print(arr)

arr = np.array([3,5,12])
arr = arr.astype("int8")
print(arr)
arr.dtype

arr = np.array([3,5,12,782])
arr = arr.astype("int8")
print(arr)
arr.dtype





## create different type of arrays

# Arange
print(np.arange(10))

print(np.arange(1,10))

print(np.arange(1,10,2))

print(np.arange(20,5,-1))

print(list(range(1,10,0.5)))

print(np.arange(1,10,0.5))

# Zeros
print(np.zeros(shape=5))

print(np.zeros(shape=(3,4)))

# np.ones
print(np.ones(5))

print(np.ones((3,4)))

# np.full
print(np.full(5,2))

print(np.full((3,4), 5))

# Linspace
print(np.linspace(0, 100, 14))

# random numbers
np.random.randint(1,100)

np.random.randint(1,100,size=10)

np.random.randint(1,100,size=(5,4))

np.random.randint(1,100,size=(2,5,4))

np.random.randint(1,100,size=(5,4))

np.random.seed(1)

np.random.randint(1,100,size=(5,4))

# Reshape

arr = np.arange(1,41)

arr

arr.reshape((4,10))

arr.reshape((10,4))

arr.reshape((5,6))

arr.reshape((2,5,4))

arr.reshape((10,-1))

## Aggregation in numpy

# sum, min, max, average, count, std, var
sales = np.array([450,1200,780,435,136])

sales

sales.sum()

np.sum(sales)    # numpy function

sum(sales)        # python function

sales.min()

sales.max()

sales.mean()   #avearage of array

sales.std()

sales.var()

sales.size   # count the elements

## Indexing And Slicing

sales

sales[1]

sales[-1]

sales[2] = 300

sales

sales[1:4]

## Indexing And Slicing in 2D

arr = np.arange(1,21).reshape((5,4))
print(arr)

arr[1]

arr[1][2]

arr

arr[1,2]

print(arr)
arr[0:2,2]

arr[0:5,2]

arr[ : :2,::2]

## Array filtering

sales = np.array([450,  99, 300, 435, 136])
sales

sales > 400

sales

sales[sales>400]

# Creating an array of age with random numbers from 12 to 50
age = np.random.randint(12,25,10)
print(age)

# find all age above or equal to 18


# find all the even age?
age[age%2==0]

## Views In Numy

arr = np.array([7,9,0,2,4,6,12,5])
print(arr)

arr_view = arr[0:4]
print(arr_view)

arr_view[1] = 55

print(arr)
print(arr_view)

## Broadcasting In Numpy

sales = np.array([450,1200,780,435,136])

print(sales)

print(sales*2)

print(sales/5)

a = np.array([4,5,6,7])
b = np.array([9,1,5,3])
a*b

a = np.array([4,5,6,7])
b = np.array([[9,1,6,6],[21,67,7,7]])

print(a)
print()
print(b)
print()

print(a+b)

## np.where

sales = np.array([450,1200,780,435,136])

np.where(sales>500,"high","Low")

# make an array of can vote and can not vote using age
age = np.array([17, 12, 23, 24, 14, 12, 16, 17, 15, 19])


print(sales)
np.where(sales>500,sales*0.2,sales*0)

# Find which numbers are even or odd from 1 to 10 ?
a = 10