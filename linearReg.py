#import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt   
def estimate_coefficient(x,y):
    n=np.size(x);
    mx,my=np.mean(x),np.mean(y)
    SSxy=np.sum(y*x)-n*mx*my
    SSxx=np.sum(x*x)-n*mx*mx
    b1=SSxy/SSxx
    b0=my-b1*mx
    
    return(b0,b1)
    
def plotGraph(x,y,b):
    y_pred=b[0]+b[1]*x
    plt.scatter(x,y)
    plt.plot(x,y_pred)
    plt.show()
    
def main():
    x=np.array([10,13,45,47,55,67,97])
    y=np.array([21,22,56,59,47,79,89])
    b=estimate_coefficient(x,y)
    print("Values of b0 & b1 are:%f,%f"%(b[0],b[1]))
    plotGraph(x,y,b)
    
if __name__=="__main__":
    main()