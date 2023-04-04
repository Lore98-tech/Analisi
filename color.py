import random

def tavola():
    print("Seleziona tavolozza di colori:")
    print("0) Scala di grigi")
    print("1) Scala di rossi")
    print("2) Scala di verdi")
    print("3) Scala di blu")
    print("4) Scala blu - fucsia")
    print("5) Scala rosso - giallo")
    print("6) Scala verde - giallo")
    print("7) Scala blu - azzurro")
    print("8) Scala verde - azzurro")
    print("9) Scala rosso- fucsia")
    print("10) Colore random")
    j = input()
    return (int(j))

def color(n, k, j):
    if j == 0:
        color = (k/(n + 1), k/(n + 1), k/(n + 1))
    elif j == 1:
        color = (k/(n + 1), 0, 0)
    elif j == 2:
        color = (0, k/(n + 1), 0)
    elif j == 3:
        color = (0, 0, k/(n + 1))
    elif j == 4:
        color = (k/(n + 1), 0, 1)
    elif j == 5:
        color = (1, k/(n + 1), 0)
    elif j == 6:
        color = (k/(n + 1), 1, 0)
    elif j == 7:
        color = (0, k/(n + 1), 1)
    elif j == 8:
        color = (0, 1, k/(n + 1))
    elif j == 9:
        color = (1, 0, k/(n + 1))
    elif j == 10:
        color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    else:
        print("Tavolozza di colori non valida.")
    return color
        
