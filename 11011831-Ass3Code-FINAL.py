import numpy as np

### Prob1: How to replace items that satisfy a condition with another value in numpy array ?
# Replace all odd numbers in arr with -1   (note this is not asking for the odd numbered positions, but the values itself)
# Input:            arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Desired output:   array([0, -1, 2, -1, 4, -1, 6, -1, 8, -1])
#
# Sources: alternative 1:: None 
#          alternative 2:: https://www.numpy.org/devdocs/reference/generated/numpy.place.html#numpy.place
#                          
print("\n\n  ----------  Problem 1  ----------  \n")
# alternative 1 :: broadcasting ops only
print("Alternative 1...")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr = (arr%2 * (arr+1) * -1) + arr
print(arr)
# alternative 2 :: use where np.place
print("Alternative 2...")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.place(arr, arr % 2 == 1, [-1])
print(arr)

## -------------------------------------------------------------------------------------------------- ##

### Prob2: How to reshape an array ?
# Convert a 1D array to a 2D array with 2 rows
# Input:            arr = np.arange(10)
# Desired output:   array([ [0, 1, 2, 3, 4],[5, 6, 7, 8, 9] ])
#
# Sources: https://www.numpy.org/devdocs/user/quickstart.html#quickstart-shape-manipulation
#
print("\n\n  ----------  Problem 2  ----------  \n")
# alternative 1 :: use reshape method, using -1 tells numpy to calculates other dimension, note that needs reassignment unlike resize
print("Alternative 1...")
arr = np.arange(10)
arr = arr.reshape(2,-1)
print(arr)
# alternative 2 :: use resize method, cannot use -1 argument so using arr.size, but note needs no reassignment
print("Alternative 2...")
arr = np.arange(10)
arr.resize(2,int(arr.size/2))
print(arr)

## -------------------------------------------------------------------------------------------------- ##

### Prob3: How to generate custome sequences in numpy without hardcoding ?
# Create the following pattern without hardcoding. Use only numpy functions and the below input array
# arr = np.array([1, 2, 3])
# Desired output:   array( [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3] )
#
# Sources: https://www.numpy.org/devdocs/reference/generated/numpy.concatenate.html#numpy.concatenate
#          https://www.numpy.org/devdocs/reference/generated/numpy.repeat.html?highlight=ndarray%20tile
#          https://www.numpy.org/devdocs/reference/generated/numpy.tile.html?highlight=ndarray%20tile
#
print("\n\n  ----------  Problem 3  ----------  \n")
#
# alternative 1:
print("Alternative 1...")
arr = np.array([1, 2, 3])
res = np.concatenate((np.repeat(arr, 3), np.tile(arr, 3)), axis=None)
print(res)
# alternative 2:
print("Alternative 2...")
arr = np.array([1, 2, 3])
res = np.r_[np.repeat(arr, 3), np.tile(arr, 3)]
print(res)

## -------------------------------------------------------------------------------------------------- ##

### Prob4: How to get the common items between two python numpy arrays ?
# Create the following pattern without hardcoding. Use only numpy functions and the below input array
# Get the common items between a and b
# a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
# b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
# Desired output:   array( [2, 4] )
#
# Sources: https://www.numpy.org/devdocs/reference/routines.set.html?highlight=set
#          https://www.numpy.org/devdocs/reference/generated/numpy.intersect1d.html#numpy.intersect1d
#          https://www.numpy.org/devdocs/reference/generated/numpy.unique.html#numpy.unique
#
print("\n\n  ----------  Problem 4  ----------  \n")
#
# alternative 1:
print("Alternative 1...")
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
res = np.intersect1d(a, b)
print(res)
# alternative 2: using np.unique first to reduce number of elements to compare
print("Alternative 2...")
res1 = np.intersect1d(np.unique(a), np.unique(b))
print(res1)

## -------------------------------------------------------------------------------------------------- ##

### Prob5: How to get the positions where elements of two arrays match ?
# Create the positions where elements of a and b match
# Get the common items between a and b
# a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
# b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
# Desired output:   array( [1, 3, 5, 7], )
#
# Sources: https://www.numpy.org/devdocs/reference/generated/numpy.where.html#numpy.where
#
print("\n\n  ----------  Problem 5  ----------  \n")
#
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
res = np.where(a==b)
print(res)

## -------------------------------------------------------------------------------------------------- ##

### Prob6:
# How to create a 2D array containing random floats between 5 and 10 ?
# Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10
#
# Sources: https://www.numpy.org/devdocs/reference/random/generated/numpy.random.mtrand.RandomState.random_sample.html#numpy.random.mtrand.RandomState.random_sample
#          https://www.numpy.org/devdocs/reference/random/legacy.html#legacy
#          https://www.numpy.org/devdocs/reference/random/generated/numpy.random.mtrand.RandomState.randint.html#numpy.random.mtrand.RandomState.randint
#          https://www.numpy.org/devdocs/reference/random/generated/numpy.random.mtrand.RandomState.random_integers.html#numpy.random.mtrand.RandomState.random_integers
#
# np.random.random_sample(size=None)
#          -- Return random floats in the half-open interval [0.0, 1.0), continuous uniform distri.
#          -- To sample Unif[a, b), b > a multiply the output of random_sample by (b-a) and add a
# np.random.randint(low, high=None, size=None, dtype='l')
#          -- Return random integers from low (INCLUSIVE) to high (EXCLUSIVE).
#          -- Return random integers from the “discrete uniform” distribution of the specified dtype in the
#             “half-open” interval [low, high). If high is None (the default), then results are from [0, low).
# np.random.random_integers(low, high=None, size=None)
#          -- DEPRECATED so use RANDINT.
#          -- Random integers of type np.int between low and high, both INCLUSIVE.
#          -- only for the closed interval [low, high], and 1 is the lowest value if high is omitted.
#
print("\n\n  ----------  Problem 6  ----------  \n")
#
lowerBound = 5.0
upperBound = 10.0
arr = (upperBound - lowerBound) * np.random.random_sample(size=(5, 3)) + lowerBound
print(arr)

## -------------------------------------------------------------------------------------------------- ##

### Prob7: How to limit the number of items printed in output of numpy array to 6 ?
# Limit the number of items printed in python numpy array a to a maximum 6 elements.
# arr = np.arange(15)
# Desired output: array([0, 1, 2, ..., 12, 13, 14])
#
# Sources: https://www.numpy.org/devdocs/reference/generated/numpy.set_printoptions.html?highlight=print#numpy.set_printoptions
#
print("\n\n  ----------  Problem 7  ----------  \n")
#
arr = np.arange(15)
print(arr)
np.set_printoptions(threshold=6)
print(arr)
# restore options to default values
np.set_printoptions(edgeitems=3, infstr='inf', linewidth=75, nanstr='nan', precision=8, suppress=False, threshold=1000, formatter=None)

## -------------------------------------------------------------------------------------------------- ##

### Prob8: How to pretty print a numpy array by supressing the scientific notation (like 1e10) ?
# Force the items printed in python numpy array to 6 significant digits.
# np.random.seed(100)
# rand_arr = np.random.random([3,3]) / 1e3
# Desired output: array([ [0.000543, 0.000278, 0.000425], [0.000845, 0.000005, 0.000122], [0.000671, 0.000826, 0.000137] ])
#
# Sources: https://www.numpy.org/devdocs/reference/generated/numpy.set_printoptions.html?highlight=print#numpy.set_printoptions
#
print("\n\n  ----------  Problem 8  ----------  \n")
#
np.random.seed(100)
rand_arr = np.random.random([3,3]) / 1e3
print(rand_arr)

np.set_printoptions(precision=6)
np.set_printoptions(suppress=True)
print(rand_arr)
# restore options to default values
np.set_printoptions(edgeitems=3, infstr='inf', linewidth=75, nanstr='nan', precision=8, suppress=False, threshold=1000, formatter=None)

## -------------------------------------------------------------------------------------------------- ##

### Prob9: How to swap two columns in a 2D numpy array ?
# Swap the columns 1 and 2 in the array arr.
# arr = np.arange(9).reshape(3,3)
#
# Sources: alternative 1:: None
#          alternative 2:: https://www.numpy.org/devdocs/reference/generated/numpy.copy.html?highlight=copy#numpy.copy
#          alternative 3:: https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-150.php
#
print("\n\n  ----------  Problem 9  ----------  \n")
#
arr = np.arange(9).reshape(3,3)
swapColA = 1
swapColB = 2
# alternative 1: without creating a new vector
print("Alternative 1...")
####
#   suppose that here a and b are the vectors in columns CA and CB
#   CA                               CB
#   a                                b
#   CA= CA +CB =a +b                 CB= CA -CB =a+b -b =a
#   CA= CA -CB =a+b -a =b            CB= CB already a= a """
####
print(arr)
arr[:,swapColA] = arr[:,swapColA] + arr[:,swapColB]
arr[:,swapColB] = arr[:,swapColA] - arr[:,swapColB]
arr[:,swapColA] = arr[:,swapColA] - arr[:,swapColB]
print("After column swapping...")
print(arr)
# alternative 2: using a new vector with deep copy
print("Alternative 2...")
arr = np.arange(9).reshape(3,3)
print(arr)
newVec = arr[:,swapColA].copy() # Using DEEP COPY with .copy() otherwise value will be overwritten later.
arr[:,swapColA] = arr[:,swapColB]
arr[:,swapColB] = newVec
print("After column swapping...")
print(arr)
# alternative 3: most elegant way - found on the net
print("Alternative 3...")
arr = np.arange(9).reshape(3,3)
print(arr)
arr[:,[swapColA, swapColB]] = arr[:,[swapColB, swapColA]]
print("After column swapping...")
print(arr)

## -------------------------------------------------------------------------------------------------- ##

### Prob10: How to swap two rows in a 2D numpy array ?
# Swap the rows 1 and 2 in the array arr.
# arr = np.arange(9).reshape(3,3)
#
# Sources: alternative 1:: None
#          alternative 2:: https://www.numpy.org/devdocs/reference/generated/numpy.copy.html?highlight=copy#numpy.copy
#          alternative 3:: https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-150.php
#
print("\n\n  ----------  Problem 10  ----------  \n")
#
arr = np.arange(9).reshape(3,3)
swapRowA = 1
swapRowB = 2
# alternative 1: without creating a new vector
print("Alternative 1...")
####
#   suppose that here a and b are the vectors in columns RA and RB
#   RA                               RB
#   a                                b
#   RA= RA +RB =a +b                 RB= RA -RB =a+b -b =a
#   RA= RA -RB =a+b -a =b            RB= RB already a= a """
####
print(arr)
arr[swapRowA,:] = arr[swapRowA,:] + arr[swapRowB,:]
arr[swapRowB,:] = arr[swapRowA,:] - arr[swapRowB,:]
arr[swapRowA,:] = arr[swapRowA,:] - arr[swapRowB,:]
print("After row swapping...")
print(arr)
# alternative 2: using a new vector with deep copy
print("Alternative 2...")
arr = np.arange(9).reshape(3,3)
print(arr)
newVec = arr[swapRowA,:].copy() # Using DEEP COPY with .copy() otherwise value will be overwritten later.
arr[swapRowA,:] = arr[swapRowB,:]
arr[swapRowB,:] = newVec
print("After row swapping...")
print(arr)
# alternative 3: most elegant way - found on the net
print("Alternative 3...")
arr = np.arange(9).reshape(3,3)
print(arr)
arr[[swapRowA, swapRowB],:] = arr[[swapRowB, swapRowA],:]
print("After row swapping...")
print(arr)