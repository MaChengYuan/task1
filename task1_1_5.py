'''
it cost O(n^2) to run bubble sort
but in best cast it can be O(n) complexity 

due to computer , i set iteration only 200 times 
'''


import time
import random
import matplotlib.pyplot as plt
import numpy as np

Time = 5
x_coordinate = []
y_coordinate = []
y_average=[]


def bubbleSort(arr):
    n = len(arr)
 
    swapped = False
  
    for i in range(n-1):
    
        for j in range(0, n-i-1):
 
     
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
                
                
        if not swapped:

            return
 
 

def init_bubble(start=1,end=2001):
    for i in range(start,end):
        shape=(1,i)
        x=np.random.randint(0,9,shape) #create matrix with random number
        Start=time.time()
        x_coordinate.append(i)
        bubbleSort(x[0])
        y_coordinate.append(time.time()-Start)
        
       

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
    init_bubble(1,201)
    plt.plot(x_coordinate,y_coordinate)
    plt.xlabel('iteration')
    plt.ylabel('time')

    # for i in range(0,Time):
    #     init_bubble()

    # print(len(y_coordinate))
    # average_()
    # plt.plot(x_coordinate[:2000],y_average)
    # plt.xlabel('iteration')
    # plt.ylabel('time')


        

if __name__ == "__main__":
    main()