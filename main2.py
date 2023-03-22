import os

for i in range(0,11):
    #os.mkdir(f"data/Day{i+1}") Here we have created multiple files in a data folder#
    os.rename(f"data/Day{i+1}",f"data/Tutorial{i+1}")