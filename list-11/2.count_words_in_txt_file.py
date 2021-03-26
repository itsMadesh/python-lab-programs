# 2. Write a function in Python to count and display the total number of words in a text file.

def count_words():
    file = open("readme.txt", "r")
    count = 0
    for line in file:
        words = line.split()
        for word in words:
            count += 1
    print("Total words are", count)

def display_words(k):
    file = open("readme.txt","r")
    a=[]
    for line in file:
        words = line.split()
        for word in words:
            if len(word) < k:
               a.append(word)
    print("This list contains whose words are less than",k,"characters:\n",a)
count_words()
k=int(input("Enter a value:"))
display_words(k)
