import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
x = linspace(0, 4, 70)
y = sin(x)
b = x
c = x - x**3/(3*2*1)
d = x - x**3/(3*2*1) + x**5/(5*4*3*2*1)
e = x - x**3/(3*2*1) + x**5/(5*4*3*2*1) - x**7/(7*6*5*4*3*2*1)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$')
plt.plot(x, y)
plt.plot(x, y, color = "#FFA6C9")
plt.plot(x, b, color = "#000000")
plt.plot(x, c, color = "#0000FF")
plt.plot(x, d, color = "#FF0000")
plt.plot(x, e, color = "#00FF00")
plt.show()
