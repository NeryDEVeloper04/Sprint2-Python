import sys
import time
import os

LISTA = [1,2,3,4,5,6,7]

def auto():
    print('auto')

def pets():
    print('pets')
    

def estudo():
    print('estudo')


def retrato():
    print('retrato')


def paisagens():
    print('paisagens')


def manual():
    print('manual')


def carregarsistema(acao):
    if acao == 'carregar':
        for _ in range(3):
            for pontos in range(4):
                sys.stdout.write(f"\rCarregando{'.' * pontos}")
                sys.stdout.flush() 
                time.sleep(0.5)
        print("\rConcluído!")
    if acao == 'sair':
        for _ in range(3):
            for pontos in range(4):
                sys.stdout.write(f"\rSaindo{'.' * pontos}")
                sys.stdout.flush() 
                time.sleep(0.5)
        print("\rConcluído!")






if __name__=='__main__':

    while True:
        print('-' * 31)
        func = int(input(f'\rDigite qual função você deseja:\nAutomático -- 1\nPets -- 2\nEstudo -- 3\nRetrato -- 4\nPaisagens -- 5\nManual -- 6\nSair -- 7\n{"-" * 31}\n'))
        if func == LISTA[6]:
            os.system('cls')
            carregarsistema('sair')
            break
        if func in LISTA:
            os.system('cls')
            carregarsistema('carregar')
            if func == LISTA[0]:
                auto()
            elif func == LISTA[1]:
                pets()
            elif func == LISTA[2]:
                estudo()
            elif func == LISTA[3]:
                retrato()
            elif func == LISTA[4]:
                paisagens()
            elif func == LISTA[5]:
                manual()
        else:
            print('Identificado que o valor digitado não corresponde a nenhuma de nossas funções. Favor digitar um número correto')

