class Quadrado:
    def __init__(self):
        self.tamlado = 0
    def muda_lado(self,lado):
        self.tamlado = lado
    def area_lado(self):
        area = self.tamlado * self.tamlado
        return self, area

quadrado_primeiro = Quadrado()
print(quadrado_primeiro)
quadrado_primeiro.muda_lado(6)
print(quadrado_primeiro.area_lado())
quadrado_primeiro.muda_lado(5)
print(quadrado_primeiro.area_lado())