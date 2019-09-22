import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from used_data_set.predefined import LINEAR_DATASET
#read the data from the stored location

dataset = pd.read_csv(LINEAR_DATASET)

X = dataset['Head Size(cm^3)'].values
Y = dataset['Brain Weight(grams)'].values

def _get_coefficient():
    #total number of values
    x_mean = np.mean(X)
    y_mean = np.mean(Y)
    n = len(X)
    # using the formula to calculate the b1 and b0
    numerator = 0
    denominator = 0
    for i in range(n):
        numerator += (X[i] - x_mean) * (Y[i] - y_mean)
        denominator += (X[i] - x_mean) ** 2

    b1 = numerator / denominator
    b0 = y_mean - (b1 * x_mean)
    return b1,b0



def _get_matplot_of_data(b1, b0):
    x_max = np.max(X) + 100
    x_min = np.min(X) - 100
    # calculating line values of x and y
    x = np.linspace(x_min, x_max, 1000)
    y = b0 + b1 * x
    plt.plot(x, y, color='#00ff00', label='Linear Regression')
    plt.scatter(X, Y, color='#ff0000', label='Data Point')
    # x-axis label
    plt.xlabel('Head Size (cm^3)')
    # y-axis label
    plt.ylabel('Brain Weight (grams)')
    plt.legend()
    plt.show()

def _calulate_rmse(b1,b0):
    #to calculate error we use root mean square error
    rmse = 0
    for i in range(n):
        y_pred=  b0 + b1* X[i]
        rmse += (Y[i] - y_pred) ** 2
        rmse = np.sqrt(rmse/n)
    return rmse


def _sum_of_squares(b1,b0):
    sumofsquares = 0
    sumofresiduals = 0
    for i in range(n) :
        y_pred = b0 + b1 * X[i]
        sumofsquares += (Y[i] - y_mean) ** 2
        sumofresiduals += (Y[i] - y_pred) **2

    score  = 1 - (sumofresiduals/sumofsquares)
    return score

def _liner_regression_with_error_calculation():
    b1,b0=_get_coefficient()
    print(b1,b0)
    #print(_get_matplot_of_data(b1,b0))
    print(_calulate_rmse(b1,b0))
    print(_sum_of_squares(b1,b0))