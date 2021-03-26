# 1. Write a function in python to read the content from a text file "poem.txt" line by line
# and display the same on screen.

def read_file():
    file = open("readme.txt", "r")
    for line in file:
        print(line, end="")
    file.close()


read_file()
