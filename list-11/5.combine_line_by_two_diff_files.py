
with open("list-11//file1.txt") as fp1, open("list-11//file2.txt") as fp2:
    for l1, l2 in zip(fp1, fp2):
        print(l1+l2)
