import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
x = linspace(0, 7, 70)
y = cos(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$ un $cos(x)$')
plt.plot(x, y)
plt.plot(x, y, color = "#FFA6C9")

y2 = sin(x)
plt.plot(x, y2, color = "#A1C5F9")

plt.legend(['$cos(x)$','$sin(x)$'])
plt.show()
