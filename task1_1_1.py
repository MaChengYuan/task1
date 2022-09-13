'''
when we create matrix , it cost O(Row * Column) complexity 

'''


import time
import random
import matplotlib.pyplot as plt
import numpy as np

Time = 5
x_coordinate = []
y_coordinate = []
y_average=[]

# count average of each 2000 iterations 
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
        



#create vector 
def create_vec(start=1,end=2001):
    for i in range(start,end):
       start = time.time()
       shape=(1,i)
       x = np.random.randint(0,9,shape)
       x_coordinate.append(i)
       y_coordinate.append(time.time()-start)
       print(x)
       print(time.time()-start) 
       

       
   
def main():
    for i in range(0,Time):
        create_vec()

    print(len(y_coordinate))
    average_()
    plt.plot(x_coordinate[:2000],y_average)e
    plt.xlabel('iteration')
    plt.ylabel('time')

        


if __name__ == "__main__":
    main()

