import random
class Tamagushi:
    def __init__(self):
        self.nome = ''
        self.fome = 0
        self.saude = 0
        self.idade = 0
    def altera_nome(self,nome):
        self.nome = nome
    def altera_fome(self,fome):
        self.fome = self.fome + fome
        if self.fome > 10:
            self.fome = 10
        elif self.fome < 0:
            self.fome = 0
    def altera_saude(self,saude):
        self.saude = self.saude + saude
        if self.saude > 10:
            self.saude = 10
        elif self.saude < 0:
            self.saude = 0
    def altera_idade(self,idade):
        self.idade = self.idade + idade
        if self.idade > 10:
            self.idade = 10
    def mostra_nome(self):
        return(self.nome)
    def mostra_fome(self):
        return(self.fome)
    def mostra_saude(self):
        return(self.saude)
    def mostra_idade(self):
        return(self.idade)

### programa
bichinho = Tamagushi()
print('*'*20,'TAMAGUSHI','*'*20)
bichinho.nome = input('Qual o nome do bichinho')
opcao = 0
while True:
    print('-'*40)
    opcao = int(input('----MENU----\n1 - Mostrar bichinho\n2 - Alimentar\n3 - Rolar tempo\n4 - Sair\n'))
    if opcao == 1:
        humor = (bichinho.mostra_fome() + bichinho.mostra_saude()) / 2
        print('Nome {}\nFome {}\nHumor {}\nSaude {}\nIdade {}'.format(bichinho.mostra_nome(),bichinho.mostra_fome(),humor,bichinho.mostra_saude(),bichinho.mostra_idade()))
    elif opcao == 2:
        bichinho.altera_fome(3)
        bichinho.altera_saude(2)
    elif opcao == 3:
        bichinho.altera_idade(1)
        bichinho.altera_fome(-1)
        bichinho.altera_saude(random.randint(-5,0))
    elif opcao == 4:
        break