from random import uniform
import math


def texpo():          #retorna el temps fins la seguent arribada
    lamb=13.98
    shape=1.665
    y=uniform(0,1)
    return lamb*(-math.log(y))**(1/shape)

    

def midaarribada():        #retorna la mida d una arribada
    return 1
    

def planta_desitjada():     #retorna la planta de desti d una persona
    r=uniform(0,1)
    if r<0.0217:
        desti=2
    elif 0.0217<=r<0.2826:
        desti=3
    elif 0.2826<=r<0.3043:
        desti=4
    elif 0.3043<=r<0.5435:
        desti=5
    elif 0.5435<=r<0.7174:
        desti=6
    elif 0.7174<=r<0.7391:
        desti=7
    elif 0.7391<=r<0.7609:
        desti=8
    elif 0.7609<=r<0.8043:
        desti=9
    elif 0.8043<=r<0.9783:
        desti=10
    elif 0.9783<=r<=1:
        desti=11
    return desti
