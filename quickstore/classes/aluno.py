# Definindo a classe Aluno
class Aluno:
    alunos = []  # Lista de todos os alunos

    def __init__(self, nome):
        self.nome = nome
        self._jurado = None
        self._notas = None
        self.alunos.append(self)  # Adiciona o aluno à lista de alunos
    
    def __str__(self):
        return f'------------Nome do aluno: {self.nome}----------------\nJurado: {self._jurado}  Notas: {self._notas}'
    
    @classmethod
    def listar_alunos(cls):
        # Imprime a lista de alunos com suas respectivas notas e jurados
        print(f"{'Nome do aluno'.ljust(20)} |{'Nome do jurado:'.ljust(20)} | {'Nota de elegância:'.ljust(20)} | {'Nota de desenvoltura:'.ljust(20)} | {'Nota de simpatia:'.ljust(20)} | {'Nota de item reciclável:'}")
        for aluno in cls.alunos:
            print(f'{str(aluno.nome).ljust(20)} |{str(aluno._jurado).ljust(20)} |{str(aluno._notas).ljust(20)}')
