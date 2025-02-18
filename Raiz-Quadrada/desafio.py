# Desafio de logica com Raiz Quadrada



def Raiz():

    from time import sleep

    while True:
        try:
            num = int(input('[+] Digite um número e veja a raiz quadrada dele: '))

            if num <= 0:
                print('[+] Digite apenas números positivos! Tente novamente.')
                continue

            else:
                raiz = num ** 0.5
                print(f'[+] A raiz quadrada de {num} é {raiz:.2f}.')
                
                try:
                    escolha = int(input('[+] [ 1 SAIR ] [ 2 CONTINUAR ]: '))
                    
                    if escolha not in (1, 2):
                        print('[+] Opção invalida! Tente novamente.')
                        continue

                    elif escolha == 1:
                        print('[+] Finalizando programa...')
                        sleep(3)
                        break

                    elif escolha == 2:
                        continue

                except ValueError:
                    print('[+] Digite um número inteiro valido! Tente novamente.')
                    continue

        except ValueError:
            print('[+] Digite um número inteiro valido! Tente novamente.')
            continue        

Raiz()
