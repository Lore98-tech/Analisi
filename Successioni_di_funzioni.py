import matplotlib.pyplot as plt
import numpy as np
import function as fct
import color as cl
import math

print("Successione di funzioni")
print("Inserire il numero di funzioni da visualizzare:")
n = input()
n = int(n)

print("Inserisci intervallo [a, b]:")
a = float(input("a = "))
b = float(input("b = "))

print("Plot delle funzioni")
cf = cl.tavola()
print("Plot delle derivate? 'si' o 'no'")
der = input()
if der == 'si':
    cd = cl.tavola()

for k in range(0, n):

    def funzione(x):
        y = x**2*np.sin(x/(0.1*k+1))
        return y

    f = fct.Function(funzione)
    f.plot(a, b, f.get_values_y(a, b), color = cl.color(n, k, cf))
    if der == 'si':
        f.plot(a, b, f.get_der(a, b), color = cl.color(n, k, cd))
    print(k)
    plt.pause(0.05)
#plt.title("$y=x^2\sin(x/(0.1k+1))$, $k=0,1,...,50$")
plt.show()