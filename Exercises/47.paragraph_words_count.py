# 47. From the given paragraph perform the following using built-in functions:

para = str(input("Type a paragraph :"))
# a. find the total number of words .
total_words = len(para.split())
print("The number of words in a paragraph are", total_words)
# b. capitalise the first word of each sentence
sentences = []
for s in para.split("."):
    sentences.append(s.lstrip().capitalize())
para = ". ".join(sentences)
print("after capitalizion : ", para)
# c. replace a given word with another word
word1 = input("Enter word to be replaced : ")
word2 = input("Enter replacement word : ")
print("After replacing with given word : ", para.replace(word1, word2))

# This program got executed successsfully and the output has been verified.
