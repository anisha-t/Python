# def welcome():
#     print("Hey, you are welcome here.")

# print(__name__) #So,hare the name of the file is main as it is the main file and 
#                 # from this file the functions 
#                 # and everything is geting imported so in main.py it is showing the name of  the other file
# if __name__ == "__main__":
#     welcome()

import os
folders =os.listdir("data")
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))


