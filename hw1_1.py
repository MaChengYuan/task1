import time
import random
import matplotlib.pyplot as plt
import numpy as np
x_coordinate = []
y_coordinate = []
x_coordinate1 = []
y_coordinate1 = []
x_coordinate2 = []
y_coordinate2 = []


def plot(x_coordinate,y_coordinate):
    plt.plot(x_coordinate,y_coordinate)
    plt.xlabel("range")
    plt.ylabel("time")


def create_vec(start=1,end=2000,interval=1):
    for i in range(start,end,interval):
       start = time.time()
       shape=(1,i)
       x = np.random.randint(0,1e12,shape)
       x_coordinate.append(i)
       y_coordinate.append(time.time()-start)
       print(x)
       print(time.time())   
    plt.ylim([0, 1e-3])
    plt.plot(x_coordinate,y_coordinate,label='create')   
                 

def sum_vec(start=1,end=2000,interval=1):
    for i in range(start,end,interval):
       start = time.time()
       shape=(1,i)
       x = np.random.randint(0,1e12,shape)
       x_coordinate1.append(i)
       sum = plus(x)
       print(x)
       print(time.time())         
       print(sum)
       y_coordinate1.append(time.time()-start)
       
    plt.plot(x_coordinate1,y_coordinate1,label='sum')


def plus(vector):
    row = vector.shape[0]
    width = vector.shape[1]
    sum = 0
    for i in range(row) :
        for j in range(width):
             sum = sum+j
    
    return sum


def time_vec(start=1,end=2000,interval=1):
    for i in range(start,end,interval):
       Start = time.time()
       shape=(i,3)
       x = np.random.randint(0,1e12,shape)
       product = times(x)
       x_coordinate2.append(i)
       y_coordinate2.append(time.time()-Start)
       print(x)
       print(time.time())   
       
       product = times(x)
       print(product)
       

    plt.plot(x_coordinate2,y_coordinate2,label='time')




def times(vector):
    row = vector.shape[0]
    width = vector.shape[1]
    product = 1
    for i in range(row) :
        for j in range(width):
             if(j!=0):
                 product = product*j
                 
           
    
    return product

def horner(poly, n, x):
 
    # Initialize result
    result = poly[0] 
  
    # Evaluate value of polynomial
    # using Horner's method
    for i in range(1, n):
 
        result = result*x + poly[i]
  
    return result

x_coordinate3 = []
y_coordinate3 = []
def activate_horner(start=1,end=2000,interval=1):
    for i in range(start,end,interval):
        Start=time.time()
        shape=(1,i)
        x=np.random.randint(0,1e12,shape)
        print(x)
        print(horner(x[0],x.size,1.5))
        x_coordinate3.append(i)
        y_coordinate3.append(time.time()-Start)
        

    plt.plot(x_coordinate3,y_coordinate3,label ='horner')
  
    
def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
                
                
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
x_coordinate4=[]
y_coordinate4=[]
 
# Driver code to test above55
def init_bubble(start=1,end=2000,interval=20):
    for i in range(start,end,round((end-start)/interval)):
        Start=time.time()
        shape=(1,i)
        x=np.random.randint(0,1e12,shape)
        bubbleSort(x[0])
       
        x_coordinate4.append(i)
        y_coordinate4.append(time.time()-Start)
        
       
        
    plt.plot(x_coordinate4,y_coordinate4,label='bubble')
     
    
def partition(l, r, nums):
    
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
           
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
   
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
    
def quicksort(l, r, nums):
    if len(nums) == 1:  
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  # Recursively sorting the left values
        quicksort(pi+1, r, nums)  # Recursively sorting the right values
    return nums

x_coordinate5=[]
y_coordinate5=[]
def init_quicksort(start=1,end=2000,interval=20):
    for i in range(start,end,round((end-start)/interval)):
  
        Start=time.time()
        shape=(1,i)
        x=np.random.randint(0,1e12,shape)
        print(quicksort(0,len(x[0])-1,x[0]))
        x_coordinate5.append(i)
        y_coordinate5.append(time.time()-Start)
   
              
    plt.plot(x_coordinate5,y_coordinate5,label='quicksort')
     
    

def calcMinRun(n):
   
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r
 
 

def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
 
 
def merge(arr, l, m, r):
 

    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
 
    i, j, k = 0, 0, l
 

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
 
        else:
            arr[k] = right[j]
            j += 1
 
        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
 

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
 
x_coordinate6=[]
y_coordinate6=[] 

def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
 
    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
 

    size = minRun
    while size < n:
 

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 

            if mid < right:
                merge(arr, left, mid, right)
 
        size = 2 * size
    
    
    

def init_timsort(start=1,end=2000,interval=20):
    for i in range(start,end,round((end-start)/interval)):
        Start=time.time()
        shape=(1,i)
        x=np.random.randint(0,1e12,shape)
        timSort(x[0])
        x_coordinate6.append(i)
        y_coordinate6.append(time.time()-Start)
      
        print(x[0])
        
              
    plt.plot(x_coordinate6,y_coordinate6,label='timesort')
 
 
    
MIN_MERGE = 32 

x_coordinate7 = []
y_coordinate7 = []

def matrix_multiplication(start=1 , end=2000, interval=5):
    for i in range(start,end,round((end-start)/interval)):
        shape=(i,i)
        start = time.time()
        x = np.random.randint(0,1e12,shape)
        y = np.random.randint(0,1e12,shape)
        product = x.dot(y)
        
        x_coordinate.append(i)
        y_coordinate.append(time.time()-start)

        
        plot(x_coordinate, y_coordinate)
        plt.xlabel("iteration")
        plt.ylabel("time")   
        
def main():
    # create_vec()
    # sum_vec()
    # time_vec()
    # activate_horner()
    # init_bubble()
    # init_quicksort()
    # init_timsort()
    matrix_multiplication()
    plt.legend()
    

if __name__ == '__main__':
    main()










