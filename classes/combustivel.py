class Combustivel:
    def __init__(self,tipo,valorl,quant):
        self.tipo = tipo
        self.valorl = valorl
        self.quant = quant
    def abas_valor(self,valor):
        #método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
        return valor / self.valorl
    def abas_quant(self,quant):
        #método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
        return quant * self.valorl
    def altera_tipo(self, tipo):
        self.tipo = tipo
    def altera_valor(self,valor):
        self.valorl = valor
    def altera_quant(self,quant):
        self.valor = self.valor + quant
#OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.