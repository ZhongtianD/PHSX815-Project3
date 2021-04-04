import sys
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy import signal

# main function for the Python code
if __name__ == "__main__":

    #Set a constant
    pi = np.pi
    # some initial parameters
    Nsample = 10
    Mode = 0
    Degree = 6
    sigma = 0.1

    if '-h' in sys.argv or '--help' in sys.argv :
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -Mode [Integer] Choose which function to fit (0-4)")
        print ("   -Nsample [Integer] number of samples for the function")
        print ("   -Degree [Integer] degree of the polynomial spline ")
        print ("   -sigma [number] standard deviation for the gaussian error")
        print
        sys.exit(1)
    
    if '-Mode' in sys.argv:
        p = sys.argv.index('-Mode')
        Mode = int(sys.argv[p+1])
    if '-Nsample' in sys.argv:
        p = sys.argv.index('-Nsample')
        Ns = int(sys.argv[p+1])
        if Ns > 0:
            Nsample = Ns
    if '-Degree' in sys.argv:
        p = sys.argv.index('-Degree')
        Nd = int(sys.argv[p+1])
        if Nd > 0:
            Degree = Nd+1
    if '-sigma' in sys.argv:
        p = sys.argv.index('-sigma')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 :
            sigma = ptemp
            
    #Define the function
    def fcn(x):
        if Mode == 0 :
            return np.sin(x)
        elif Mode == 1:
            return np.cos(x)
        elif Mode == 2:
            return signal.square(x)
        elif Mode == 3:
            return signal.sawtooth(5*x)
        elif Mode == 4:
            i, q, e = signal.gausspulse(x, fc=0.7, retquad=True, retenv=True)
            return i

    #Generate the samples
    X = random.uniform(-pi,pi,Nsample)
    Y = fcn(X)+random.normal(0,sigma,Nsample)
    
    #Define the least square function and make a fit
    def Leastsq(W):
        F = 0
        for i in range(Nsample):
            S = 0
            for j in range(Degree):
                S+=W[j]*(X[i]**j)
            F+=np.square(Y[i]-S)
        return F
    W = np.zeros(Degree)
    res = minimize(Leastsq,W)
    W = res.x
    #Make plot
    def sol(x):
        S = 0
        for j in range(Degree):
            S+=W[j]*(x**j)
        return S
    Line  = np.linspace(-pi,pi,100,endpoint=False)

    plt.plot(Line,sol(Line),c='g', label = "Fitted function")
    plt.plot(Line,fcn(Line),c='r',label="True function")
    plt.scatter(X,Y,label="Samples")
    
    plt.legend()
    plt.title(str(Degree) +  "th degree polynomial fitting")
    plt.savefig('Fit_result.png')
    plt.show
    
    #Calculate the reduced Chi-square statistic
    def Rchi():
        Chi = 0 
        for i in range(Nsample):
            Chi+= np.square(Y[i]-sol(X[i]))
        Chi /=(sigma)**2
        return Chi/(Nsample-Degree)
    print(Rchi())
    
    
