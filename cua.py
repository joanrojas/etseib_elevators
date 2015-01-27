import copy
class cua(object):
    def __init__(self,elems=[]):
        self.elems=copy.deepcopy(elems)
    def encua(self,element):
        self.elems.append(element)
    def desencua(self):
        return self.elems.pop(0)
    def primer(self):
        return self.elems[0]
    def __len__(self):
        return len(self.elems)
    def es_buida(self):
        return len(self)==0
    def __str__(self):
        s='Cua('
        if not self.es_buida():
            for e in self.elems:
                s+=str(e)+', '
            s=s[:-2]
        return s+')'
    def sort(self):
        self.elems.sort()
        
