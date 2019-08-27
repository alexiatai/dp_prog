class Circulo:

    def __init__(self, raio, x, y):
        self.raio = raio
        self.centro = (x, y)

    def verificar_raio(self,raio):
        if self.raio<=0:
            raio = 1

    def calcular_area(self):
        return 3.14*self.raio**2
         

raio = float(input("Entre com um valor para raio: "))
area = Circulo.calcular_area(raio)
print(area)

