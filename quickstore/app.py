from classes.aluno import Aluno
from classes.nota import Nota
from classes.jurado import Jurado

# Funções auxiliares para capturar dados do usuário
def nome_jurado():
    return input('Qual o nome do jurado: ')

def nome_aluno():
    return input('Qual o nome do aluno que deseja colocar a nota: ')

def nota_elegancia():
    return float(input('Qual a nota da elegância: '))

def nota_desenvoltura():
    return float(input('Qual a nota de desenvoltura: '))

def nota_simpatia():
    return float(input('Qual a nota de simpatia: '))

def nota_item_reciclavel():
    return float(input('Qual a nota do item reciclável: '))

# Função principal para coordenar a avaliação dos alunos pelos jurados
def main():
    jurado = Jurado(nome_jurado())  # Cria um objeto Jurado com o nome fornecido
    quantidade_de_alunos = int(input('Quantos alunos você irá dar a nota: '))  # Obtém a quantidade de alunos a serem avaliados
    
    for _ in range(quantidade_de_alunos):
        nome_aluno_atual = nome_aluno()  # Obtém o nome do aluno
        # Cria um objeto Nota com as notas fornecidas
        nota_aluno = Nota(nota_elegancia(), nota_desenvoltura(), nota_simpatia(), nota_item_reciclavel())
        aluno = Aluno(nome_aluno_atual)  # Cria um objeto Aluno com o nome fornecido
        jurado.avaliar_aluno(aluno, nota_aluno)  # Avalia o aluno
    
    outro_usuario = input('Outro jurado irá dar a nota? (s/n) ')
    if outro_usuario.lower() == 's':
        main()  # Chama a função principal novamente para outro jurado

# Início do programa
if __name__ == '__main__':
    main()  # Inicia o processo de avaliação
    Aluno.listar_alunos()  # Lista todos os alunos avaliados
    