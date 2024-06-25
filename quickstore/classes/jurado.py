# Definindo a classe Jurado
class Jurado:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'{self.nome}'
    
    def avaliar_aluno(self, aluno, notas):
        aluno._notas = notas
        aluno._jurado = self
        
        