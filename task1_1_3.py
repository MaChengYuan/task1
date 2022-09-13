'''
when we create matrix , it cost O(Row * Columns) complexity 
and it cost anohter Row * Columns to make calculation of product 
complexity will be 2(Row * Columns ) = O(Row * Columns )

'''



import time
import random
import matplotlib.pyplot as plt
import numpy as np

Time = 5
x_coordinate = []
y_coordinate = []
y_average=[]



#calculate product of total elements in matrix
def time_vec(start=1,end=2001):
    for i in range(start,end):
       Start = time.time()
       shape=(i,3)
       x = np.random.randint(0,9,shape)
       x_coordinate.append(i)
       product = times(x)
       y_coordinate.append(time.time()-Start)
       print(x) 
       print(product)
       
# time everytime two elements 
def times(vector):
    row = vector.shape[0]
    width = vector.shape[1]
    product = 1
    for i in range(row) :
        for j in range(width):
             if(j!=0):
                 product = product*j
                            
    
    return product



# average each 2000 iteration
def average_():
    global y_average
    for i in range(0,2000):
        YSum = 0
        for j in range(0,Time):           
            YSum = YSum + y_coordinate[i+(2000*j)]
            print(i+2000*j)
        print(YSum)    
        y_average.append(YSum)
        
    y_average = np.array(y_average)
    y_average = y_average / 5
    return 
        



       
def main():
    for i in range(0,Time):
        time_vec()

    print(len(y_coordinate))
    average_()
    plt.plot(x_coordinate[:2000],y_average)
    plt.xlabel('iteration')
    plt.ylabel('time')


        

if __name__ == "__main__":
    main()
