'''
i used numpy to make matrix calculation easier 
becasue of numpy , i just transpose one matrix and multiply with another 
it is easier version of naive matrix multiplication algorithm 
complexity can be O(x^3)
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



def matrix_multiplication(start=1 , end=2001):
    for i in range(start,end):
        shape=(i,i)
        start = time.time()
        x = np.random.randint(0,10,shape)
        print(x)
        y = np.random.randint(0,10,shape)
        product = x.dot(y)
        
        x_coordinate.append(i)
        y_coordinate.append(time.time()-start)
        print(product)






"""def average_():
    global y_average
    for i in range(0,2001):
        YSum = 0
        for j in range(0,Time):           
            YSum = YSum + y_coordinate[i+(2000*j)]
            print(i+2000*j)
        y_average.append(YSum)
    y_average = np.array(y_average)
    y_average = y_average / 5
    return """


       
def main():
    
    matrix_multiplication(1,201)
    plt.plot(x_coordinate,y_coordinate)
    plt.xlabel('iteration')
    plt.ylabel('time')
    
    # for i in range(0,Time):
    #    matrix_multiplication(1,2)
    # print(len(y_coordinate))
    # average_()
    # plt.plot(x_coordinate[:2000],y_average)
    # plt.plot(x_coordinate,y_coordinate) 


 

        

if __name__ == "__main__":
    main()
    