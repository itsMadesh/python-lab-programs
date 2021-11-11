from Queue import Queue
def palindrome_checker(s):
    q=Queue()
    l=len(s)
    for i in range(l//2):
        q.enqueue(s[i])
    print(q.display())
    chr=q.dequeue()
    i=l-1
    while(chr):
        if(chr!=s[i]):
            return None
        chr=q.dequeue()
        i-=1
    return 1

s=input("Enter a string:")
if(palindrome_checker(s)):
    print("{0} is palindromme".format(s))
else:
    print("{0} is not palindromme".format(s))