import numpy as np

#Euler Method
def euler(f, t0, y0, h, n):
   t = t0
   y = y0
   while n > 0:
        y += h * f(t, y)
        t +=  h
        n -= 1
   return y


#Runge-Kutta   
def runge_kutta(f, t0, y0, h, n):
   t, y = t0, y0
   while n > 0:
       k1 = h * f(t, y)
       k2 = h * f(t + h * 0.5, y + k1 * 0.5)
       k3 = h * f(t + h * 0.5,  y + k2 * 0.5)
       k4 = h * f(t + h, y + k3)

       y +=(k1 + 2 * k2 + 2 * k3 + k4) / 6.0
       t += h

       n -= 1
   return y




 
