
from cua import cua
from ascensor import ascensor
from persona2 import persona
from time import sleep
from events import tenca_portes,creaeventplanta,event_planta,event_baixa
#---------------------------------------


#set mode-------------------------------
#mode1 parells/senars mode2 altes baixes
#ascensor A parells, altes
#asensor B senars, baixes
#nsim nombre de simulacions

nsim=10000
mode='mode2'

nomfitxer='simulacio'+mode+'.txt'
f=open(nomfitxer,'w')
#set max time simulation in seconds--------------------

t_max=500

#set time between steps (seconds)------------------
#machine max vel set to 0

timestep=0


#----------------------------------------
for simulacio in range(1,nsim+1):
    firstA=True
    firstB=True
    f.write('sim_num'+str(simulacio)+'\n')
    cua_arribades=cua()
    cua_A=cua()
    cua_B=cua()
    cua_Events=cua()
    ascensor_A=ascensor()
    ascensor_B=ascensor()
    person0=persona()
    cua_arribades.encua((person0.t,person0))
    primins='temps:',cua_arribades.primer()[0],'Event type:',cua_arribades.primer()[1].type,'Planta:',cua_arribades.primer()[1].desti
    f.write(str(cua_arribades.primer()[0])+',')
    person=persona(person0.t)
    cua_Events.encua((person.t,person))
    step=0
    print 'Step:',step,'-----------------------------------------------------------------'
    print 'A',len(ascensor_A.persones),'B',len(ascensor_B.persones),'cua A',len(cua_A.elems),'cua B',len(cua_B.elems),'porta A',ascensor_A.portes,'porta B',ascensor_B.portes,'Planta A',ascensor_A.planta,'Planta B',ascensor_B.planta
    print 'Itinerari A',ascensor_A.itinerari,'Itinerari B',ascensor_B.itinerari
    f.write(str(len(cua_A.elems))+','+str(len(cua_B.elems))+'\n')
    step=1
    print '-------------------------------------------------------------------------\n'
    print primins[0],primins[1],primins[2],primins[3],primins[4],primins[5]
    sleep(timestep)
    while cua_Events.primer()[0]<t_max:
        f.write(str(cua_Events.primer()[0])+',')
        if cua_Events.primer()[1].type=='persona':
            evento= 'temps:',cua_Events.primer()[0],'Event type:',cua_Events.primer()[1].type,'Planta:',cua_Events.primer()[1].desti
        else:
            evento= 'temps:',cua_Events.primer()[0],'Event type:',cua_Events.primer()[1].type
        if not cua_Events.es_buida():
            typ=cua_Events.primer()[1].type
            if typ=='persona':
                t,person=cua_Events.desencua()
                cua_arribades.encua((t,person))
                person=persona(t)
                cua_Events.encua((person.t,person))
            elif typ=='tenca_portes':
                asc=cua_Events.primer()[1].asce
                t=cua_Events.primer()[0]
                if asc=='A':
                    cua_Events.desencua()[1].tenca(ascensor_A)
                    print 'itinerari A',ascensor_A.itinerari
                    #crear events de passar per plantes
                    creaeventplanta(t,ascensor_A,'A',cua_Events)
                elif asc=='B':
                    cua_Events.desencua()[1].tenca(ascensor_B)
                    print 'itinerari B',ascensor_B.itinerari
                    #crear events de passar per plantes
                    creaeventplanta(t,ascensor_B,'B',cua_Events)
            elif typ=='event_planta':
                t,planta=cua_Events.desencua()
                asc=planta.asce
                if asc=='A':
                    ascensor_A.planta=planta.planta
                    ascensor_A.descarrega()
                    if len(ascensor_A.persones)==0 and ascensor_A.portes=='T' and ascensor_A.planta!=0:
                        cua_Events.encua((t+ascensor_A.planta*ascensor_A.tempsperplantabuit,event_baixa('A')))
                elif asc=='B':
                    ascensor_B.planta=planta.planta
                    ascensor_B.descarrega()
                    if len(ascensor_B.persones)==0 and ascensor_B.portes=='T' and ascensor_B.planta!=0:
                        cua_Events.encua((t+ascensor_B.planta*ascensor_B.tempsperplantabuit,event_baixa('B')))
            elif typ=='event_baixa':
                t,asc=cua_Events.desencua()
                if asc.asce=='A':
                    firstA=False
                    ascensor_A.planta=0
                    ascensor_A.portes='O'
                    for i in range(ascensor_A.capacitat):
                        if not cua_A.es_buida():
                            ascensor_A.carrega(cua_A.desencua()[1])
                        else:
                            break
                elif asc.asce=='B':
                    firstB=False
                    ascensor_B.planta=0
                    ascensor_B.portes='O'
                    for i in range(ascensor_B.capacitat):
                        if not cua_B.es_buida():
                            ascensor_B.carrega(cua_B.desencua()[1])
                        else:
                            break
        if not cua_arribades.es_buida():
            person=cua_arribades.primer()[1]
            if mode=='mode1':
                ascens=person.planta_mode1
            elif mode=='mode2':
                ascens=person.planta_mode2
            if ascens=='A':
                cua_A.encua(cua_arribades.desencua())
                if ascensor_A.planta==0 and ascensor_A.portes=='O':
                    t,person=cua_A.desencua()
                    ascensor_A.carrega(person)
                    #crea events de passar per plantes
                    if ascensor_A.portes=='T' and firstA and len(ascensor_A)<ascensor_A.capacitat:
                        creaeventplanta(t,ascensor_A,'A',cua_Events)
                    cua_Events.encua((person.t+ascensor_A.tenca,tenca_portes('A')))
                    for ind in range(len(cua_Events.elems)):
                        event=cua_Events.elems[ind]
                        if event[0]<person.t+ascensor_A.tenca and event[1].type=='tenca_portes':
                            cua_Events.elems.pop(ind)
                            break
            elif ascens=='B':
                cua_B.encua(cua_arribades.desencua())
                if ascensor_B.planta==0 and ascensor_B.portes=='O' and len(ascensor_B)<ascensor_B.capacitat:
                    t,person=cua_B.desencua()
                    ascensor_B.carrega(person)
                    #crea events de passar per plantes 
                    if ascensor_B.portes=='T' and firstB:
                        creaeventplanta(t,ascensor_B,'B',cua_Events)
                    cua_Events.encua((person.t+ascensor_B.tenca,tenca_portes('B')))
                    for ind in range(len(cua_Events.elems)):
                        event=cua_Events.elems[ind]
                        if event[0]<person.t+ascensor_B.tenca and event[1].type=='tenca_portes':
                            cua_Events.elems.pop(ind)
                            break
        cua_Events.elems.sort()
        #per modelitzar el temps entre plantes
        #ascensor_A.tempsperplantaple=flin(len(ascensor_A.itinerari)
        f.write(str(len(cua_A.elems))+','+str(len(cua_B.elems))+'\n')
        print 'Step:',step,'-----------------------------------------------------------------'
        print 'A',len(ascensor_A.persones),'B',len(ascensor_B.persones),'cua A',len(cua_A.elems),'cua B',len(cua_B.elems),'porta A',ascensor_A.portes,'porta B',ascensor_B.portes,'Planta A',ascensor_A.planta,'Planta B',ascensor_B.planta
        print 'Itinerari A',ascensor_A.itinerari,'Itinerari B',ascensor_B.itinerari
        step+=1
        print '-------------------------------------------------------------------------\n'
        if evento[3]=='persona':
            print evento[0],evento[1],evento[2],evento[3],evento[4],evento[5]
        else: print evento[0],evento[1],evento[2],evento[3]
        print '-------------------------------------------------------------------------'
        sleep(timestep)
f.close()
