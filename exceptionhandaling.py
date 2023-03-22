a = input("Enter your number :")
print(f"The multiplication table of {a} is : ")

try :
    for i in range (1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except ValueError:
    print("You have entered a wrong input value")

