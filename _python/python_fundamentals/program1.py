Loops_iterations= input("How many  times do you want loop ?")
print ("Your want to loop:", Loops_iterations)
Loops_iterations=int(Loops_iterations)

#Function Fibonacci Numbers
#Fn = Fn-1 + Fn-2

def Fibonacci_Numbers(x):

    if x == 1:
        #print(x)
        return 1
    elif x==2:
        #print(x)
        return 1
    else:
        return Fibonacci_Numbers(x-1) + Fibonacci_Numbers(x-2)

#t = Fibonacci_Numbers(x)
#print(t)

for i in range(1,Loops_iterations+1):
       n=Fibonacci_Numbers(i)
       print(n)

import math

def area_of_circle(r):
    """Function that defines an area of a circle"""
    a = r**2 * math.pi
    return a

print area_of_circle(1)
#Examples:

#1! = 1

#2! = 1×2 = 2

#3! = 1×2×3 = 6

#4! = 1×2×3×4 = 24

#5! = 1×2×3×4×5 = 120

#Recursive factorial formula
#n! = n×(n-1)!

#Example:

#5! = 5×(5-1)! = 5×4! = 5×24 = 120
def Area_function(x,y):
    area = x * y
    return area

print("x = 5 and y=5")
square_area = Area_function(5,5)
print(square_area)