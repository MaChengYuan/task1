import time
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
x_coordinate = np.linspace(1, 2000, 2000, endpoint=True)
y_coordinate = []
x_coordinate1 = []
y_coordinate1 = []
x_coordinate2 = []
y_coordinate2 = []

def Const(x,b):
    return 0*x +b
def Linear(x,a,b):
    return a*x+b
def Nlong(x, a, b, c):
    return a * x * np.log(b * x) + c
def Square(x, a, b, c):
    return a * x**2 + b * x + c
def theoretical(x,a,b,c,d):
    return a*x**3 + b*x**2 +c*x +d

def plot(x_coordinate,y_coordinate,theoretical_function,label):
 
    function = theoretical_function
    x_coordinate = np.array(x_coordinate)
    # y_coordinate = np.array(y_coordinate)
    popt, pcov = curve_fit(function, x_coordinate, y_coordinate)

    plt.plot(x_coordinate,y_coordinate,label=label)
    plt.plot(x_coordinate, function(x_coordinate, *popt), color="maroon", label="theoretical")

    plt.xlabel("range")
    plt.ylabel("time")
    plt.legend()
    plt.show()

def create_vec(start=1,end=2001,interval=1):
    y = []
    for i in range(start,end,interval):
       start = time.time()
       shape=(i,)
       x = np.random.randint(0,1,shape)
       # print(x) 
       y.append(time.time()-start)
  
       # print(time.time()) 
    y_coordinate.append(y)
                 

def sum_vec(start=1,end=2001,interval=1):
    y = []
    for i in range(start,end,interval):
       Start = time.time()
       shape=(i,)
       x = np.random.randint(0,2000,shape)
       x_coordinate1.append(i)
       Sum = np.sum(x)
       y.append(time.time()-Start)   
      
    y_coordinate1.append(y)




def time_vec(start=1,end=2001,interval=1):
    y=[]
    for i in range(start,end,interval):
       Start = time.time()
       x = np.random.randint(0,2000,i)
       product = np.prod(x)

       y.append(time.time()-Start)   
    y_coordinate2.append(y)
    



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
def activate_horner(start=1,end=2001,interval=1):
    y=[]
    for i in range(start,end,interval):
        Start=time.time()
        shape=(1,i)
        x=np.random.randint(0,2000,shape)
        # print(x)
        # print(horner(x[0],x.size,1.5))
        y.append(time.time()-Start)   
      
    y_coordinate3.append(y)

  
    
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
            # print(arr)
                
                
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
x_coordinate4=[]
y_coordinate4=[]
 
# Driver code to test above55
def init_bubble(start=1,end=2001,interval=1):
    y=[]
    for i in range(start,end,interval):
        Start=time.time()
        shape=(i,)
        x=np.random.randint(0,2000,shape)
        bubbleSort(x)       
        y.append(time.time()-Start)   
      
    y_coordinate4.append(y)
    
     
    
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
def init_quicksort(start=1,end=2001,interval=1):
    y=[]
    for i in range(start,end,interval):
  
        Start=time.time()
        shape=(i,)
        x=np.random.randint(0,2000,shape)
        quicksort(0,len(x)-1,x)
        y.append(time.time()-Start)   
      
    y_coordinate5.append(y)

     
    

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
    
    
    

def init_timsort(start=1,end=2001,interval=1):
    y=[]
    for i in range(start,end,interval):
        Start=time.time()
        shape=(i,)
        x=np.random.randint(0,2000,shape)
        timSort(x)
        y.append(time.time()-Start)   
       
    y_coordinate6.append(y)

        
 
 
    
MIN_MERGE = 32 

x_coordinate7 = []
y_coordinate7 = []

def matrix_multiplication(start=1 , end=2001, interval=1):
    z=[]
    for i in range(start,end,interval):
        shape=(i,i)
        Start = time.time()
        x = np.random.randint(0,2000,shape)
        y = np.random.randint(0,2000,shape)
        product = x.dot(y)
        
        z.append(time.time()-Start)   
       
    y_coordinate7.append(y)  
    
  
def average_time(y_coordinate,theory,label,x_coordinate=x_coordinate):
    y = []
    for i in range(len(y_coordinate[1])):
        Sum = 0
        for j in range(len(y_coordinate)):
            Sum += y_coordinate[j][i]
        y.append(Sum/len(y_coordinate))
    print(len(y))
    plot(x_coordinate,y,theory,label=label)  
 


def main():

    for i in range(5):
        create_vec()  
        sum_vec()
        time_vec()
        activate_horner()
        init_bubble()
        init_quicksort()
        init_timsort()
        matrix_multiplication()
    average_time(y_coordinate,Const,"create")
    average_time(y_coordinate1,Linear,"sum")

    average_time(y_coordinate2,theoretical ,"product")
    average_time(y_coordinate3,theoretical,"horner")
    x_coordinate4 = np.linspace(1, 40, 40, endpoint=True)
    average_time(y_coordinate4,theoretical,"bubble")
    average_time(y_coordinate5,Nlong,"quick")
    average_time(y_coordinate6,Nlong,"time")
    average_time(y_coordinate7,theoretical,"matrix_mul")
    

if __name__ == '__main__':
    main()










