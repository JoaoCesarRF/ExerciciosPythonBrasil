import math
class Retangulo:
    def __init__(self):
        self.ladoa = 0
        self.ladob = 0
    def mudar_lado(self,lado,valor):
        if lado == 'a':
            self.ladoa = valor
        elif lado == 'b':
            self.ladob = valor
    def mostra_lado(self,lado):
        if lado == 'a':
            return self.ladoa
        elif lado == 'b':
            return self.ladob
    def area(self):
        area = self.ladoa * self.ladob
        return area
    def perimetro(self):
        perimetro = (self.ladoa * self.ladob) / 2
        return perimetro
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
#Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

while True:
    piso = Retangulo()
    area = Retangulo()
    print('Calculadora de piso')
    piso.mudar_lado('a',int(input('Digite a largura do piso em cm')))
    piso.mudar_lado('b',int(input('Digite a comprimento do piso em cm')))
    area.mudar_lado('a', float(input('Digite a largura da area em cm')))
    area.mudar_lado('b', float(input('Digite a comprimento da area em cm')))
    print('Sao necessarios {} pisos para cobrir a area'.format(math.ceil((area.area() / piso.area()))))
    sair = input('Deseja s para Sair')
    if sair.upper() == 'S':
        break

