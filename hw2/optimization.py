from scipy.optimize import minimize
import numpy as np

def rosen(X):
    """
    Define Rosenbrock function with n = 3
    :param x: array
    :return: value of the function
    """
    return (1.0 - X[0])**2 + 100.0 * (X[1] - X[0]**2)**2 + (1.0 - X[1])**2 + 100.0 * (X[2] - X[1]**2)**2

def grad(x):
    """
    Define the gradident of Rosenbrock function with n=3
    :param x: list 
    :return: list of length of 3
    """
    return np.array([-400 * x[0] * x[1] + 400 * x[0] ** 3 - 2 * (1 - x[0]),
                     -400 * x[1] * x[2] + 400 * x[1] ** 3 - 2 * (1 - x[1]) + 200 * (x[1] - x[0] ** 2),
                     200 * (x[2] - x[1] ** 2)])

if __name__ == '__main__':
    
    n = 10 
    Min = 1000000

    for i in range(n):
        x = np.random.uniform(-50, 50, size=(3, 1))
        res = minimize(rosen, x0=x, method='BFGS', jac = grad)
        val = rosen(res.x)
        print (val,res.x)
        if val < Min:
            Min = rosen(res.x)
            point = res.x
            start = x
            
    print("Best minimized value for the Rosenbrock function: ", Min)
    print("Minimizing point: ", point)
    print("Corresponding start point is: ", start)
