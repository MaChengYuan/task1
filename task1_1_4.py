'''

Time complexity of this approach is O(n2) if we use a simple loop for evaluation of x^n

'''



import time
import random
import matplotlib.pyplot as plt
import numpy as np

Time = 5
x_coordinate = []
y_coordinate = []
y_average=[]



def horner(poly, n, x):
 
    # Initialize result
    result = poly[0] 
  
    # Evaluate value of polynomial
    # using Horner's method
    for i in range(1, n):
 
        result = result*x + poly[i]
  
    return result


def activate_horner(start=1,end=2001):
    for i in range(start,end):
        shape=(1,i)
        x=np.random.randint(0,9,shape) #create matrix with random nunmbers
        Start=time.time()
        x_coordinate.append(i)
        
        print(horner(x[0],x.size,1.5))
        y_coordinate.append(time.time()-Start)
        
        print(x)

    

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
        activate_horner()

    print(len(y_coordinate))
    average_()
    plt.plot(x_coordinate[:2000],y_average)



        

if __name__ == "__main__":
    main()