from scipy.optimize import minimize
import numpy as np

def rosen(X):
    """
    Define Rosenbrock function with n = 3
    :param x: array
    :return: value of the function
    """
    return (1.0 - X[0])**2 + 100.0 * (X[1] - X[0]**2)**2 + (1.0 - X[1])**2 + 100.0 * (X[2] - X[1]**2)**2

if __name__ == '__main__':
    
    n = 10 
    Min = 1000000

    for i in range(n):
        x = np.random.uniform(-10, 10, size=(3, 1))
        res = minimize(rosen, x0=x, method='BFGS')
        val = rosen(res.x)
        print (val,res.x)
        if val < Min:
            Min = rosen(res.x)
            point = res.x
            start = x
            
    print("Best minimized value for the Rosenbrock function: ", Min)
    print("Minimizing point: ", point)
    print("Corresponding start point is: ", start)
