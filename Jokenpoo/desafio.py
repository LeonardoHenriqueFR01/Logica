# Desafio Jokenpoo

from time import sleep
from random import randint


def Venceu():
    print('-' * 50)
    print(f'{"VENCEU":^50}')
    print('-' * 50)

    print(f'[+] Sua jogada {jogadas[user]}')
    print(f'[+] Jogada da maquina {jogadas[maquina]}')


def Perdeu():
    print('-' * 50)
    print(f'{"PERDEU":^50}')
    print('-' * 50)
    
    print(f'[+] Sua jogada {jogadas[user]}')
    print(f'[+] Jogada da maquina {jogadas[maquina]}')


def Empate():
    print('-' * 50)
    print(f'{"EMPATE":^50}')
    print('-' * 50)
    
    print(f'[+] Sua jogada {jogadas[user]}')
    print(f'[+] Jogada da maquina {jogadas[maquina]}')


def Mine_Game():

    global user, maquina, jogadas
   
    perdas = ganhos = empates = 0

    jogadas = {1:'PEDRA', 2:'PAPEL', 3:'TESOURA'}

    while True:
        try:
            user = int(input('[+] [ 0 SAIR ] [ 1 PEDRA ] [ 2 PAPEL ] [ 3 TESOURA ]: '))

            maquina = randint(1, 3)

            if user == 0:
                print('[+] Finalizando programa...')
                sleep(3)
                break

            elif user not in (0, 1, 2, 3):
                print('[+] Opção invalida! Tente novamente.')
                continue

            if (user == 1 and maquina == 3) or (user == 2 and maquina == 1) or (user == 3 and maquina == 2):
                print('[+] Maquina jogando...')
                sleep(2)
                Venceu()
                ganhos += 1

                try:
                    escolha = int(input('[+] [ 1 SAIR ] [ 2 CONTINUAR ]: '))

                    if escolha == 1:
                        print(f'[+] Total de ganhos {ganhos}.')
                        print(f'[+] Total de perdas {perdas}.')

                        print('[+] Finalizando programa...')
                        sleep(3)
                        break

                    elif escolha == 2:
                        continue

                    elif escolha not in (1, 2):
                        print('[+] Opção invalida! Tente novamente.')
                        continue

                except ValueError:
                    print('[+] Digite um número inteiro valido! Tente novamente.')
                    continue
            
            elif (user == 3 and maquina == 1) or (user == 1 and maquina == 2) or (user == 2 and maquina == 3):
                print('[+] Maquina jogando...')
                sleep(2)
                Perdeu()
                perdas += 1

                try:
                    escolha = int(input('[+] [ 1 SAIR ] [ 2 CONTINUAR ]: '))

                    if escolha == 1:
                        print(f'[+] Total de ganhos {ganhos}.')
                        print(f'[+] Total de perdas {perdas}.')
                        
                        print('[+] Finalizando programa...')
                        sleep(3)
                        break

                    elif escolha == 2:
                        continue

                    elif escolha not in (1, 2):
                        print('[+] Opção invalida! Tente novamente.')
                        continue

                except ValueError:
                    print('[+] Digite um número inteiro valido! Tente novamente.')
                    continue

            elif user == maquina:
                print('[+] Maquina jogando...')
                sleep(2)
                Empate()
                empates += 1

                try:
                    escolha = int(input('[+] [ 1 SAIR ] [ 2 CONTINUAR ]: '))

                    if escolha == 1:
                        print('[+] Finalizando programa...')
                        sleep(2)
                        break

                    elif escolha == 2:
                        continue

                    elif escolha not in (1, 2):
                        print('[+] Opção invalida! Tente novamente.')
                        continue
                
                except ValueError:
                    print('[+] Digite um número inteiro valido! Tente novamente.')
                    continue

        except ValueError:
            print('[+] Digite um número inteiro valido! Tente novamente.')
            continue


Mine_Game()
