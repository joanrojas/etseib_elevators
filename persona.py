from random import uniform
def nombrepersonesinv(u):
    if u<0.2:
        return 1
    if 0.2<=u<0.4:
        return 2
    if 0.4<=u<0.7:
        return 3
    if 0.7<=u<0.8:
        return 4
    if 0.8<=u<0.85:
        return 5
    if 0.85<=u<0.95:
        return 6
    if 0.95<=u<=1:
        return 7
class persona(object):
    def __init__(self):
        r=uniform(0,1)
        if r<0.06:
            self.desti=2
        elif 0.06<=r<0.26:
            self.desti=3
        elif 0.26<=r<0.46:
            self.desti=4
        elif 0.46<=r<0.76:
            self.desti=5
        elif 0.76<=r<0.81:
            self.desti=6
        elif 0.81<=r<0.86:
            self.desti=7
        elif 0.86<=r<0.91:
            self.desti=8
        elif 0.91<=r<0.96:
            self.desti=9
        elif 0.96<=r<0.98:
            self.desti=10
        elif 0.98<=r<=1:
            self.desti=11
        self.type='persona'
