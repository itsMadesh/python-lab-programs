import sys
fp=open("file6.txt","w")
a=sys.argv[1]
fp.write(a)
fp.close()
word_occur=sys.argv[2]
fp1=open("file6.txt","r")
occurence=0  
contents=fp1.read()
words=contents.split(" ")
for i in words:
    if(i==word_occur):
        occurence+= 1
print("Word",word_occur,"occured in a given file is", occurence)

      

