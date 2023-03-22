fruit = "Apple"
len1 = len(fruit)
print("The length of fruit is : ",len1)
#Slicing of the string Apple

#Including from 0 to 6-1
print(fruit[0:6])
#Including from 0 to 3
print(fruit[0:3])
#Including from 0 to 5
print(fruit[:])
#Including from 5-1 = 4 to 5-3 =2 which is not possible it will not print
print(fruit[-1:-3])
#Including from 5-3 = 2 to 5-1 =4
print(fruit[-3:-1])
