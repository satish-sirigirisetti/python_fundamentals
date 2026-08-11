import numpy as np
# Easy 

# [1] Create a numpy array containing numbers from 1 to 10

a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a)

# [2] multiply every element by 5

a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a*5)

#[3] add two arrays [1,2,3] and [4,5,6]

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)

#[4] find the square of every element in [2,4,6]

a=np.array([2,4,6])
squar=np.square(a)
print(squar)

#[5] find all the lements greater than 20

a=np.array([10,20,30]) 
print(a[a>20])

# Hard

#[6] find the sum,mean,maximum and minimum of [12,15,18,21,24]

a=np.array([12,15,18,21,24])
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))

#[7] Create a 3*3 matrix and calculate row wise and coloum wise

a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))

#[8] Reshape an array of numbers from 1 to 12 into 3*4 matrix

a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b=a.reshape(3,4)
print(b)

#[9] flatten 3*3 matrix into 1D array 

a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
b=a.flatten()
print(b)

#[10] sort the array [7,2,9,5,1]

a=np.array([7,2,9,5,1])
print(np.sort(a))

#[11] perform matrix multiplication

a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
b=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])

print(np.matmul(a,b))

#[12] find the dot product of [2,3,4] and [5,6,7]
a=np.array([2,3,4])
b=np.array([5,6,7])
print(np.dot(a,b))

#[13] Use boolean indexing tpo extract all even numbers from an array
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
even=a%2==0

print(a[even])

#[14] Stack two arrays vertically and horizontally
a=np.array([2,3,4])
b=np.array([5,6,7])
print(np.vstack((a,b)))
print(np.hstack((a,b)))

#[15] split an array of 12 elements into 4*4 matrix

a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b=np.split(a,4)
print(b)

#[16] find the uniq elements in [1,2,2,3,4,4,5]
a=np.array([1,2,2,3,4,4,5])
b=np.unique(a)
print(b)

#[17] find the index of maximun and minimum values in an array

a=np.array([1,2,2,3,4,4,5])
b=a.max()
c=np.where(a==b)
print(c)

#[19] apply the np.sqrt,np.log,np.exp

a=np.array([1,2,2,3,4,4,5])
print(np.sqrt(a))
print(np.log(a))
print(np.exp(a))

#[20]  Create two arrays that uses broadcasting to produce a 3*3 matrix 
a=np.array([[1],[2],[3]])
b=np.array([1,2,3])
print(a+b)

#BROADCASTING AND VECTORISATION 

#[1] scalar broadcasting 

a=np.array([1,2,3,4,5])
print(a+5)

#[2] Row broadcasting 

a=np.array([[1,2,3],
            [4,5,6]])
b=np.array([10,20,30])
print(a+b)

#[3] coloumn broadcasting 

a=np.array([[1],
            [2]])
b=np.array([3,4])
print(a+b)

#[4] vectorisation 

a=np.array([5,10,15,20])
b=np.array([1,2,3,4])
print(a+b)
print(a*b)
print(a/b)

#[5] combined

a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(a+5)

print(np.square(a))

print(np.sum(a,axis=1))

print(np.mean(a,axis=0))
