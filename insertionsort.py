from random import sample
from matplotlib import pyplot
from time import process_time
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        for j in range(i,-1):
            if key > arr[j]:
                c = j + 1
                break
            arr[j+1] = arr[j]
        else:
            c = 0
        arr[c] = key
if __name__ == "__main__":
    y = []
    x=range(1,10000,100)
    for i in x:
        testlist = sample(range(1,1000*i),i)
        start = process_time()
        insertion_sort(testlist)
        y.append((process_time() - start))
    pyplot.plot(x,y)
    pyplot.xlabel=('Length of array')
    pyplot.ylabel=('time taken in ms')
    pyplot.show()