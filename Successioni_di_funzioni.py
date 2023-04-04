import matplotlib.pyplot as plt
import numpy as np
import function as fct
import color as cl

print("Successione di funzioni")
print("Inserire il numero di funzioni da visualizzare:")
n = input()
n = int(n)

#range di valori
print("Inserisci intervallo [a, b]:")
a = float(input("a = "))
b = float(input("b = "))

print("Plot delle funzioni")
cf = cl.tavola()
print("Plot delle derivate")
cd = cl.tavola()

for k in range(0, n + 1):

    def funzione(x):
        #y = (1/(1-x)*x*x - x/(2 - x * x))
        #y = np.sin(k *x)
        #y = np.power(np.power(k*x, 2) + 1, 1/2) - np.power(np.power(k*x, 2) - 1, 1/2)
        #y = x/(1 + k * x)
        #y = x/(1 + np.power(k*x, 2))
        #y = np.power(k*x, 2)/(1 + np.power(k*x, 2))
        #y = np.power((np.power(x, 2) - x),k)
        #y = k*k/x
        #y = np.sin(np.power(x, 2)/k) + (1 - np.power(1 - np.power(x, 2), 1/2))/k #[-1; 1]
        #y = np.sin(np.power(x, 2)/k)
        #y = (k * np.power(x, 3) + np.power((k + 1), 2) * np.sin(x))/(1 + np.power(k, 2)) #[-1; 1]
        y = np.power(k, 3)/(np.power(k, 1) * 2 * x) * np.sin(x) + x * np.power((k + 1), 2)/(1 + np.power(k, 2)) - np.log(k * np.abs(x))
        return y

#funzione
    f = fct.Function(funzione)
    f.plot(a, b, f.get_values_y(a, b), color = cl.color(n, k, cf))
    f.plot(a, b, f.get_der(a, b), color = cl.color(n, k, cd))
    #print(f.asintoti(a, b))
    #f.asintoti_plot(a, b)
plt.show()