class Pessoa:
    def  __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self,anos):
        if self.idade < 21:
            self.idade = self.idade + anos
            self.altura = self.altura + (anos * 0.5)
        else:
            self.idade = self.idade + anos
    def engordar(self,kgs):
        self.peso = self.peso + kgs
    def emagrecer(self,kgs):
        self.peso = self.peso - kgs
    def crescer(self,tam):
        self.altura = self.altura + tam
#Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
primeiro = Pessoa()
primeiro.nome = 'Joao'
print(primeiro.idade)
primeiro.envelhecer(9)
print(primeiro.altura)
primeiro.envelhecer(9)
print(primeiro.altura)
print(primeiro.idade)