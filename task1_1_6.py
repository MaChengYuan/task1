'''
average , best , worst complexity of quick sort is O(nlogn)

'''


import time
import random
import matplotlib.pyplot as plt
import numpy as np

Time = 5
x_coordinate = []
y_coordinate = []
y_average=[]


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
        quicksort(l, pi-1, nums)  
        quicksort(pi+1, r, nums)  
    return nums

def init_quicksort(start=1,end=2001):
    for i in range(start,end):
        shape=(1,i)
        x=np.random.randint(0,9,shape) #create matrix with random number
        Start=time.time()
        x_coordinate.append(i)
        print(quicksort(0,len(x[0])-1,x[0]))
        y_coordinate.append(time.time()-Start) #count the total cost time 
    

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

       
def main():
    init_quicksort(1,201)
    plt.plot(x_coordinate,y_coordinate)
    plt.xlabel('iteration')
    plt.ylabel('time')

    # for i in range(0,Time):
    #    init_quicksort()
    # print(len(y_coordinate))
    # average_()
    # plt.plot(x_coordinate[:2000],y_average)
    # plt.xlabel('iteration')
    # plt.ylabel('time')


        

if __name__ == "__main__":
    main()



