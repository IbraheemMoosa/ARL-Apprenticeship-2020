# Credit to user:pyland on StackOverflow

import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np
import math

#https://www.multpl.com/s-p-500-historical-prices/table/by-year

x_vals = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
y_vals = np.array([1425,1335,1140,895,1132,1181,1278,1424,1378,865,1123,1282,1300,1480,1822,2028,1918,2275,2789,2607,3278])

plt.plot(x_vals, y_vals, "ko", label="Data")
plt.savefig("s&p-1.svg")

# Create an x-axis
x_axis = np.linspace(0, x_vals.max(), 100)

#Create a function y = ab^x+c as a benchmark
def func(x,a,b,c):
    return a*np.exp(b*x) + c

benchmark_func = func(x_axis,5,.3,1500)
plt.plot(x_axis, benchmark_func, "-", label="Benchmark")
plt.savefig("s&p-2.svg")


# Using built in LSR
initial_vals = [5,.3,1500]
w, _ = opt.curve_fit(func, x_vals, y_vals, p0=initial_vals)
print("Estimated Values: ", w)

optimized_func = func(x_axis, 2.232e+1, 2.292e-1, 1.113e+3)
plt.plot(x_axis, optimized_func, "-", label="Optimized")
plt.savefig("s&p-3.svg")
