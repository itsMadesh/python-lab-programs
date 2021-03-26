import sys
print(sys.argv)

arr = []
with open("list-11/file4.txt", "r") as fp:
    for line in fp.readlines():
        arr.append(int(line))


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


bubbleSort(arr)
with open("list-11/file4.txt", "a") as fp:
    fp.write("\n"+"\n".join([str(e) for e in arr]))
