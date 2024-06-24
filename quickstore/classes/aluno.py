class Aluno:

    notas_jurados = []

    def __init__(self,nome,jurado,notas):
        self.nome = nome
        self.jurado = jurado
        self.notas = notas
        self.notas_jurados.append(self)
    
    def __str__(self):
        return f'------------Nome do aluno: {self.nome}----------------\nJurado: {self.jurado}  Notas: {self.notas}'
    
    @classmethod
    def listar_alunos(cls):
        print(f"{'Nome do aluno'.ljust(20)} |{'Nome do jurado'.ljust(20)} | {'Nota de elegancia:'.ljust(20)} | {'Nota de desenvoltura:'.ljust(20)} | {'Nota de simpatia:'.ljust(20)} | {'Nota de item reciclavel:'}")
        for nota in cls.notas_jurados:
            print(f'{str(nota.nome).ljust(20)} | {str(nota.jurado).ljust(20)} | {str(nota.notas).ljust(20)} ')
