class tenca_portes(object):
    def __init__(self,asc):
        self.type='tenca_portes'
        self.asce=asc
    def tenca(self,asce):
        asce.portes='T'
def creaeventplanta(t_act,ascensor,asc,cua_Events):
    llista_de_plantes=ascensor.itinerari
    llista_de_plantes.sort()
    te=ascensor.tempsperplantaple
    planta_vella=0
    for planta in llista_de_plantes:
        t_act+=te*(planta-planta_vella)
        print t_act,planta
        cua_Events.encua((t_act,event_planta(planta,asc)))
        planta_vella=planta
class event_planta(object):
    def __init__(self,planta,asc):
        self.asce=asc
        self.planta=planta
        self.type='event_planta'
class event_baixa(object):
    def __init__(self,asc):
        self.type='event_baixa'
        self.asce=asc
