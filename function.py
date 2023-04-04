import matplotlib.pyplot as plt
import numpy as np
import math
import time

step = 0.001
limite = 50

class Function:
    def __init__(self, callback):
        self._x = []
        self.callback = callback
    
    def get_value(self, value):         #calcola il valore della funzione nel punto 'value'
        return self.callback(value)

    def get_values_x(self, a, b):       #crea una stringa con i punti dell'intervallo [a,b] 
        if len(self._x) == 0:
            i = 0
            while (a + i * step) <= b:
                self._x.append(a + i * step)
                i = i + 1
            self._x = np.array(self._x)
        return self._x

        
    def get_values_y(self, a, b):   #crea una stringa con i valori della funzione
        yf = []
        i = 0
        while (a + i * step) <= b:
            try:
                y = self.get_value(a + i * step)
            except Exception as e:
                print(e)
                y = 10 * limite
            yf.append(y)
            i = i + 1
        return np.array(yf)
    
    def get_der(self, a, b):    #fa la derivata della funzione restituendo una stringa con i suoi valori
        x = self.get_values_x(a, b)
        ydf = []
        for i in range(len(x) - 1):
            try:
                yd = (self.get_value(x[i + 1]) - self.get_value(x[i]))/(step)
            except Exception as e:
                print(e)
                yd = 10 * limite
            ydf.append(yd)
            i = i + 1
        ydf = np.array(ydf)
        ydf = np.append(ydf ,np.nan)
        return ydf
    
    def plot(self, a, b, y, **color):
        x = self.get_values_x(a, b)
        c = 0
        if np.amax(np.abs(y) > limite):
            c = 1
        y[np.abs(y) > limite] = np.nan
        if len(color) == 0:
            plt.plot(x, y)
        else:
            plt.plot(x, y, color = color.get("color", color))
        if c == 1:
            plt.ylim(- limite, limite)
        return 0

    def asintoti(self, a, b):
        x = self.get_values_x(a, b)
        y = self.get_values_y(a, b)
        s = []
        c = 0
        i = 0
        while i < (len(y) - 1):
            if np.abs(y[i]) > 2*limite and np.abs(y[i+1]) > 2*limite:
                j = i
                while np.abs(y[j]) > 2*limite and np.abs(y[j+1]) > 2*limite:
                    c = c + 1
                    j = j + 1
                s.append(x[int(j-c/2)])
                c = 0
                i = j + 1
            if np.abs(y[i]) > 2*limite and np.abs(y[i+1]) <= 2*limite:
                s.append(x[i])
                i = i + 1
            else:
                i = i + 1
        s = np.array(s)
        return s

    def plot_asintoti(self, a, b):
        r = self.asintoti(a, b)
        for i in range(len(r)):
            plt.axvline(r[i], -limite, limite, color = "orange", linewidth = 0.5, linestyle = "--")
        return 0