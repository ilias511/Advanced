import numpy as np

a = np.array([1,5,9])
#print(a)

ones = np.ones(20,dtype=np.int64)

#print(ones)
#.reshape(4,5))

empty = np.empty(5)
print(empty)

arrange = np.arange(2,9,2) # it goes from start to end-1 with step 2
#print(arrange)


linspace = np.linspace(0,10) # create an array with values that are spaced linearly in a specified interval
#print(linspace)

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
#print(np.concatenate((arr1,arr2)))

#print(arr1[::-1])
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

five_up = (c>=6)  # one way
print(c[five_up])

divisible_by_2 = c[c%2==0] # another way
print(divisible_by_2)
