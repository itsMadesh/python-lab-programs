def partition(array, low, high):

    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quickSort(array, low, high):
    if low < high:

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)

def array(n):
    data=[]
    for i in range(n):
        x=int(input("Enter a value in index-"+str(i)+":"))
        data.append(x)
    return data

n=int(input("Enter no.of inputs:"))
data=array(n)
print("Unsorted array:", data)
quickSort(data, 0, n - 1)
print('Sorted Array in Ascending Order:')
print(data)
