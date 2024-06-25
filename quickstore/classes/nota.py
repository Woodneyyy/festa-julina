# Definindo a classe Nota
class Nota:
    def __init__(self, elegancia, desenvoltura, simpatia, item_reciclavel):
        self.elegancia = elegancia
        self.desenvoltura = desenvoltura
        self.simpatia = simpatia
        self.item_reciclavel = item_reciclavel

    def __str__(self):
        return f'Nota de elegância: {self.elegancia} | Nota de desenvoltura: {self.desenvoltura} | Nota de simpatia: {self.simpatia} | Nota de item reciclável: {self.item_reciclavel}'