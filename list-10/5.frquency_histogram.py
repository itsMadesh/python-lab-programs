#5. Frequency histogram 

sentence=input("Enter a sentence:")
word=sentence.split()

d = dict()
for c in word:
   if c not in d:
       d[c] = 1
   else:
       d[c] += 1
print(d)