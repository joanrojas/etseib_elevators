import aleatori
import math
from random import uniform
from scipy.stats import expon
from rule import parellsenar,altbaix
class persona(object):
    def __init__(self,t=0,lamb=14.8,shape=1.665):
    
         lamb=14.8
         shape=1.665
         y=uniform(0,1)
         tentre= lamb*(-math.log(y))**(1/shape)
    
         self.desti=aleatori.planta_desitjada()
         self.type='persona'
         self.t=t+tentre
         self.planta_mode1=parellsenar(self.desti)
         self.planta_mode2=altbaix(self.desti)
         

#A parells, altes
#B senars, baixes
