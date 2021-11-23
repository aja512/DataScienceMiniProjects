import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
# %matplotlib inline

def estimate_coefficient(x,y):
    n=np.size(x);
    mx,my=np.mean(x),np.mean(y)
    SSxy=np.sum(x*y)-n*mx*my
    SSxx=np.sum(x*x)-n*mx*mx
    b1=SSxy/SSxx
    b0=my-b1*mx
    return(b0,b1)
    
def plotGraph(x,y,b0,b1):
    y_pred=b0+b1x
    plt.scatter(x,y)
    plt.plot(x,y_pred)
    plt.show()

def main():
    x=np.array([10,13,45,47,55,67,97])
    y=np.array([21,22,56,59,47,79,89])
    b0,b1=estimate_coefficient(x,y)
    print("Values of b0 & b1 are:"+format(b0,b1))
    plotGraph(x,y,b0,b1)
    
if __name__=="main":
    main()