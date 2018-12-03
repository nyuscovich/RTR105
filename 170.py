# Fails: 170.py 
# Autors: Nikola Juskoviča 
# Apliecibas numurs: 181REB291 
# Datums: 03/12/2018
# Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

# -*- coding: utf -8 -*-
from math import sin, fabs
from time import sleep

def f(x):
    return sin(x)

# Definejam argumenta x robezhas:
a = 1.1
b = 3.2

# Aprekjinam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)

# Paarbaudam, vai dotajaa intervaala ir saknes:
if ( funa * funb > 0.0) :
    print ("Dotajaa intervaale [%s, %s] saknju nav")%(a,b)
    sleep(1); exit()    # Zinjo uz ekraana, gaida 1 sec. un darbu pabeidz
else:
    print ("Dotajaa intervaalaa sakne(s) ir!")

# Defineejam precizitaati, ar kaadu mekleesim sakni:
deltax = 0.01
k = 0

# Sashaurinam saknes mekleeshanas robezhas:
while ( fabs(b-a) > deltax ) :
    k = k + 1
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0.0 ):
        b = x
    else:
        a = x

print ("Sakne x ir: ", x)
print ("f(x) = ", f(x))
print ("iteraciju skaits: ", k)
