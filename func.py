def geometric_Mean (a,b):
    mean = a*b/a+b
    print(mean)

def is_greater(a,b):
    if(a>b):
        print("first number is greater than second number")
    else:
        print("second number is greater than first number")

a1=int(input("Enter your num1:"))
b1=int(input("Enter your num2:"))
geometric_Mean(a1,b1)
is_greater(a1,b1)

