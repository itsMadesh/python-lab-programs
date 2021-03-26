# 3. Write a function display_words() in python to read lines from a text file "story.txt",
# and display those words, which are less than 4 characters.

def display_words():
    file = open("readme.txt","r")
    for line in file:
        words = line.split()
        for word in words:
            if len(word) < 4:
               print(word, end=" ")

display_words()

