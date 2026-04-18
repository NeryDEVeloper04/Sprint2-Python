import sys
import time
import os

LISTA = [1,2,3,4,5,6,7]
botao = False

def carregarsistema(acao):


    for _ in range(3):
        for pontos in range(4):
            sys.stdout.write(f"\r{acao}{'.' * pontos}")
            sys.stdout.flush() 
            time.sleep(0.5)
    print('\nConcluído!')



def auto():
    """Função automática, implementação de IA na camêra para identificação de melhor modo para a foto"""
    print('auto')



def pets():
    """Função pets, utilizada para fotos com pets e animais, com implementação de botão sonoro para chamar atenção dos animais"""
    botao = False
    botao = input('Clicar em botão sonoro? S (sim)| N (não)\n').lower()
    if botao == 's':
        botao = True

    elif botao == 'n':
        botao = False

    else:
        botao = False

    if botao == True:
        #Chamando função para chamar pet
        carregarsistema('Chamando pet')


    return 'configurações ajustadas para pet'
    
def estudo():
    """Função Pets, futuro uso de OCR para identificar e ler imagens, transformando em PDF ou documentos(estudando complexidade)"""
    print('estudo')


def retrato():
    """Função retrato, ajuste de configurações da câmera que melhor se encaixam para retrato"""
    print('retrato')


def paisagens():
    """Função paisagens, ajuste de configurações da câmera que melhor se encaixam para paisagens"""

    print('paisagens')


def manual():
    """Função manual, função para ajuste da câmera pelo próprio usuario"""
    print('manual')








if __name__=='__main__':

    while True:
        os.system('cls')
        print('-' * 31)
        func = int(input(f'\rDigite qual função você deseja:\nAutomático -- 1\nPets -- 2\nEstudo -- 3\nRetrato -- 4\nPaisagens -- 5\nManual -- 6\nSair -- 7\n{"-" * 31}\n'))

        if func == LISTA[6]:
            #Saindo do programa
            os.system('cls')
            carregarsistema('Saindo')
            break

        if func in LISTA:
            #Limpando terminal
            os.system('cls')
            #Carregamento
            carregarsistema('Carregando')

            if func == LISTA[0]:
                #Condição para função auto
                op = auto()

            elif func == LISTA[1]:
                #Condição para função pets
                op = pets()

            elif func == LISTA[2]:
                #Condição para função estudo
                op = estudo()

            elif func == LISTA[3]:
                #Condição para função retrato
                op = retrato()

            elif func == LISTA[4]:
                #Condição para função paisagens
                op = paisagens()

            elif func == LISTA[5]:
                #Condição para função manual
                op = manual()
            
            print(f'{op}, esperando foto...')
        else:
            print('Opção inválida.')
        
        time.sleep(5)


