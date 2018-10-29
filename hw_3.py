
# Name: Yi Jin
# Course: 37810
# hw3.py

import math
import random

##### Template for Homework 3, exercises 1 -  ######


# ********** Exercise 1 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####

def is_divisible(m,n):
	if n==0:
		print("n cannot be 0")
		return False
	if m%n==0:
		return True
	else:
		return False

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

#print is_divisible(10, 5)  # This should return True
print(is_divisible(10, 5)) 
#print is_divisible(18, 7)  # This should return False
print(is_divisible(18, 7)) 
#print is_divisible(42, 0)  # What should this return?
print(is_divisible(42, 0)) 

# ********** Exercise 2 ********** 

# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(m,n):
	if m==n:
		return False
	else:
		return True

# Test cases for not_equal
##### YOUR CODE HERE #####

print(not_equal(1,2))
#return True
print(not_equal(1000,1000))
#return False

# ********** Exercise 3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a,b,c):
	return a*b+c

## 2 - Equations
##### YOUR CODE HERE #####
angle_test=math.sin(multadd(math.pi,1/4,0))+multadd(math.cos(multadd(math.pi,1/4,0)),1/2,0)

ceiling_test=math.ceil(multadd(276,1/19,0))+multadd(2,math.log(12)/math.log(7),0)

# Test Cases

print("sin(pi/4) + cos(pi/4)/2 is:")
print(angle_test)


print("ceiling(276/19) + 2 log_7(12) is:")
print(ceiling_test)

# ********** Exercise 4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####

def rand_divis_3():
	i=random.randint(0,100)
	return is_divisible(i,3)

# Test Cases
##### YOUR CODE HERE #####
for j in range(15):
	print(rand_divis_3(),end=" ")