import time
import random
import matplotlib.pyplot as plt
'''
when we create matrix , it cost O(Row * Columns) complexity 
and it cost anohter Row * Columns to make calculation of sum 
complexity will be 2(Row * Columns ) = O(Row * Columns )

'''


import numpy as np

Time = 5
x_coordinate = []
y_coordinate = []
y_average=[]


#count the sum of each element in matrix 
def sum_vec(start=1,end=2001):
    for i in range(start,end):
       start = time.time()
       shape=(1,i)
       x = np.random.randint(0,9,shape)
       x_coordinate.append(i)
       sum = plus(x)
       print(x)
    
       
       print(sum)
       print(time.time()-start)
       y_coordinate.append(time.time()-start)
       


# plus number
def plus(vector):
    row = vector.shape[0]
    width = vector.shape[1]
    sum = 0
    for i in range(row) :
        for j in range(width):
             sum = sum+j
    
    return sum
      

# average each 2000 iteration
def average_():
    global y_average
    for i in range(0,2000):
        YSum = 0
        for j in range(0,Time):           
            YSum = YSum + y_coordinate[i+(2000*j)]
            
        y_average.append(YSum)
    y_average = np.array(y_average)
    y_average = y_average / 5
    return 


       
def main():
    for i in range(0,Time):
        sum_vec()

    print(len(y_coordinate))
    average_()
    plt.plot(x_coordinate[:2000],y_average)
    plt.xlabel('iteration')
    plt.ylabel('time')


        

if __name__ == "__main__":
    main()