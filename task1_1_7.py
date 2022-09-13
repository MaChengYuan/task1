'''
usually time complexity of time sort is O(nlogn) 
but in the best case it can be O(n)

'''


import time
import random
import matplotlib.pyplot as plt
import numpy as np


MIN_MERGE = 32 
Time = 5
x_coordinate = []
y_coordinate = []
y_average=[]




def calcMinRun(n):
   
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r
 
 

# This function sorts array from left index 
# to right index which is of size atmost RUN
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
 
 
def merge(arr, l, m, r):
    # original array is broken in two parts
    # left and right array

    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
 
    i, j, k = 0, 0, l
    # after comparing, we merge those two array
    # in larger sub array

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
 
        else:
            arr[k] = right[j]
            j += 1
 
        k += 1
    #copy remaining
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
 
    #copy remaining
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
 
 
#(similar to merge sort)
def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
 
    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
 

    # Start merging from size RUN (or 32). It will merge
    # to size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:
        
        # Pick starting point of left array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 

            if mid < right:
                merge(arr, left, mid, right)
 
        size = 2 * size
        

def init_timsort(start=1,end=2001):
    for i in range(start,end):
        shape=(1,i)
        x=np.random.randint(0,9,shape)
        Start=time.time()
        x_coordinate.append(i)
        timSort(x[0])        
        y_coordinate.append(time.time()-Start)
        print(x[0])
                    
    
# average each 2000 iteration
def average_():
    global y_average
    for i in range(0,2000):
        YSum = 0
        for j in range(0,Time):           
            YSum = YSum + y_coordinate[i+(2000*j)]
            print(i+2000*j)
        y_average.append(YSum)
    y_average = np.array(y_average)
    y_average = y_average / 5
    return 
        

def plot(x_coordinate,y_coordinate):
    plt.plot(x_coordinate,y_coordinate)
    plt.xlabel('iteration')
    plt.ylabel('time')


       
def main():
    for i in range(0,Time):
       init_timsort()
    print(len(y_coordinate))
    average_()
    plt.plot(x_coordinate[:2000],y_average)
    plt.xlabel('iteration')
    plt.ylabel('time')


        

if __name__ == "__main__":
    main()
    
