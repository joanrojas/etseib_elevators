import persona
import copy

class ascensor(object):
    def __init__(self,persones=[],capacitat=20,itinerari=[],planta=0,tempsperplantaple=8,tenca=5):
        self.planta=planta
        self.portes='O'
        self.persones=copy.deepcopy(persones)
        self.capacitat=capacitat
        self.itinerari=copy.deepcopy(itinerari)
        self.tempsperplantaple=tempsperplantaple
        self.tempsperplantabuit=tempsperplantaple/3
        self.tenca=5
        self.itinerari=[]
    def __len__(self):
        return len(self.persones)
    
    def es_buit(self):
        return len(self)==0
    
    def es_ple(self):
        return len(self)==self.capacitat

    def calculaItinerari(self):     # un cop esta carregat calcula les plantes per les que ha de passar
        l=list()
        if not self.es_buit():
            for persona in self.persones:
                if not persona.desti in l:
                    l.append(persona.desti)
            l.sort()
            self.itinerari=copy.deepcopy(l)
        else:
            print 'Ascensor buit'

    def carrega(self,persona): #carrega una persona i actualitza itinerari
        if not self.es_ple():
            self.persones.append(persona)
        else:
            self.portes='T'
            print 'Ascensor ple'
        self.calculaItinerari()
    
   
            
    def descarrega(self):   #descarrega a la planta actual i actualitza itinerari
        r=[]
        if not self.es_buit():
           for indx in range(len(self.persones)):
                persona=self.persones[indx]
                if persona.desti==self.planta:
                    r.append(indx)
           r.reverse()
           for indx in r:
                    self.persones.pop(indx) 
           self.itinerari.pop(0)        
        else:
            print 'Ascensor buit'
        
        
        
    def puja(self):   #puja una planta
        if not self.planta==11:
            self.planta+=1
    def baixa(self):             #baixa una planta
        if not self.planta==0:
            self.planta-=1
        
    
    
    

    
            
                
        
        
                
        
        
        
        
        
        
    
