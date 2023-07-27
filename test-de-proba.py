import sys
from random import choice

def affiche(n, t):
    for i in n:
        print(f'{i[0]}:{i[1]}, {(t/100)*i[1]}%')

def calcule(t=1000, n=2):
    out = []
    for i in range(n):
        out += [[str(i),0]]

    for i in range(t):
        c = choice(out)
        c[1] += 1
    
    affiche(out, t)
    return out



calcule()