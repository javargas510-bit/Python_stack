# Basic Print all intergers from  0 to 150
for i in range(0, 151, 1):
    print(i)
print("\n")

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for t in range(0, 1001, 5):
    print(t)
print("\n")

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for num in range(1,100):
    if num % 5 == 0:
        print("Coding")
    if num % 10 == 0:
        print("Coding Dojo")

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
for num in range(0,500000):
    if num % 2 != 0:
        num += num
print("FINAL SUM:",num)
print("\n")

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for j in range(2018, 0, -4):
    print(j)
print("\n")

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2 
highNum = 9
mult = 3
for num in range(lowNum,highNum+1):
    if num % mult == 0:
        print(num)


