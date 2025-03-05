
from src.main.assignment_3 import (
    euler,
    runge_kutta

)

t0 = 0
t = 2
n = 10
y0 = 1

h = (t - t0) / n

def f(t, y):
    return t - y ** 2

#Euler Method
approx_euler = euler(f, t0, y0, h, n)
print(f"{approx_euler}") 

#Runge_Kutta Method
approx_rk = runge_kutta(f, t0, y0, h, n)
print(f"{approx_rk}")