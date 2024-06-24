from classes.aluno import Aluno
from classes.nota  import Nota
from classes.jurado import Jurado

def nome_jurado():
    nome_jurado = input('qual o nome do jurado: ')
    return nome_jurado
def nome_aluno():
    nome_aluno = input('qual o nome do aluno que dejesa colocar a nota: ')
    return nome_aluno
def nota_elegancia():
    nota_elegancia = float(input('Qual a nota da elegância: '))
    return nota_elegancia
def nota_desenvoltura():
    nota_desenvoltura = float(input('Qual a nota de desenvoltura: '))
    return nota_desenvoltura 
def nota_simpatia():
    nota_simpatia= float(input('Qual a nota de simpatia: '))
    return nota_simpatia
def nota_item_reciclavel():
    nota_item_reciclavel = float(input('qual a nota do item reciclaval: '))
    return nota_item_reciclavel


def main():



    jurado = Jurado(nome_jurado())
    quantidade_de_alunos = int(input('quantos alunos você ira dar a nota: '))
    i=0
    while i<quantidade_de_alunos:
        nomealuno = nome_aluno()
        nota_aluno = Nota(nota_elegancia(),nota_desenvoltura(),nota_simpatia(),nota_item_reciclavel())
        aluno = Aluno(nomealuno)
        jurado.avaliar_aluno(aluno, nota_aluno , jurado)
        i = i+1
    outro_usuario = input('outro jurado irar dar a nota? (s/n) ')
    if outro_usuario == 's':
        main()


if __name__ == '__main__':
    main()
    Aluno.listar_alunos()
    