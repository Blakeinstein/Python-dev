import random
import time
from matplotlib import pyplot 
def merge_sort(alist, start, end):
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)
 
def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1

y = []
x=range(5,10)
for i in x:
    testlist = random.sample(range(1,100),i)
    start = time.process_time()
    merge_sort(testlist,0,len(testlist))
    y.append((time.process_time() - start)*100)

pyplot.plot(x,y)
pyplot.xlabel=('Length of array')
pyplot.ylabel=('time taken in ms')
pyplot.show()
