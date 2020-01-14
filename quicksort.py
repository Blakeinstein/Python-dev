from random import sample
from matplotlib import pyplot
from time import process_time
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        part = partition(arr, low, high)
        quick_sort(arr, low, part -1)
        quick_sort(arr, part + 1, high)
if __name__ == "__main__":
    y = []
    x=range(1,10000,100)
    for i in x:
        testlist = sample(range(1,1000*i),i)
        start = process_time()
        quick_sort(testlist,0,len(testlist)-1)
        y.append((process_time() - start))
    pyplot.plot(x,y)
    pyplot.xlabel=('Length of array')
    pyplot.ylabel=('time taken in ms')
    pyplot.show()