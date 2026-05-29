import sys
import time
import re
# Eu queria testar as importações de funções existentes a partir de outro arquivo python
from funcoes import menuInterativo as MI
# portanto já criei uma função menu para ser exibida a cada nova interação do usuário

lista = []
opcoes = (0, 1, 2, 3, 4)

while True:
    try:
        decisao = int(input('Digite qual opção deseja escolher: '))

        if decisao not in opcoes:
            print('[❌ERRO]! Digite uma opção dentre as apresentadas!\n')
            continue

        elif decisao == 2:
            if lista == []:
                print('[❌ERRO]! Nenhum participante cadastrado!\n')
                continue

        elif decisao == 3:
            if lista == []:
                print('[❌ERRO]! Nenhum participante cadastrado!\n')
                continue

        elif decisao == 4:
            if lista == []:
                print('[❌ERRO]! Nenhum participante cadastrado!\n')
                continue

        if decisao == 1:
            print(f'Você escolheu a opção ({decisao})!')
            # 1 Sistema de carregamento elaborado por mim
            print("\nCarregando", end="", flush=True)
            # e replicado em todas as opções do menu.
            for _ in range(3):
                time.sleep(1)
                print(".", end="", flush=True)
            time.sleep(1)
            print('\nSucesso!\n')

            while True:
                nome = str(
                    input('Digite qual o nome do participante: ')).title()
                if re.findall(r'[^a-zA-Zà-úÀ-Ú\s]', nome) or nome == '' or not nome.strip():
                    # 2 Esse primeiro if serviu para formartar o texto e proibir o usuário
                    print('[❌ERRO]! Somente nomes!\n')
                    # de digitar algo que não seja um texto.
                    continue
                elif nome.replace(" ", "").isalpha():
                    # 3 o elif aqui serviu para permitir que o usuário introduza espaços para abrir
                    lista.append(nome)
                    # margem a inclusão de sobrenomes (algoritmos 1, 2 e 3 irão se repetir por todo o código)
                    print('✅ Usuário adicionado!')
                    while True:
                        try:
                            novo_s = 's'
                            novo_n = 'n'
                            novo_participante = str(
                                input('\nDeseja incluir mais algúem? [S/N]: ')).lower()

                            if novo_participante != novo_s:
                                if novo_participante != novo_n:
                                    print(
                                        '[❌ERRO]! Somente sim ou não!\nTente novamente.')
                                    continue

                            if novo_participante == novo_n:
                                print(
                                    f'Você escolheu a opção ({novo_participante.upper()})!\nVamos voltar para o menu.\n')
                                print('='*89)
                                print('Sua lista atual está assim:')
                                for p in range(0, len(lista)):
                                    # Exibição da lista de forma ordenada porém ainda falta ajustar
                                    print(f'{p + 1} - {lista[p]}')
                                # a situação do index de cada item na lista, pois o número exibido
                                print('='*89)
                                # não corresponde ao mesmo item da lista.
                                print("\nCarregando", end="", flush=True)
                                for _ in range(3):
                                    time.sleep(1)
                                    print(".", end="", flush=True)
                                time.sleep(1)
                                print('\nPronto!\n')
                                time.sleep(0.5)
                                MI()
                                break
                            if novo_participante == novo_s:
                                print(
                                    f'Você escolheu a opção ({novo_participante.upper()})!\n')
                            while True:
                                if novo_participante == novo_s:
                                    nome = str(
                                        input('Digite qual o nome do participante: ')).title()
                                    if re.findall(r'[^a-zA-Zà-úÀ-Ú\s]', nome) or nome == '' or not nome.strip():
                                        print('[❌ERRO]! Somente nomes!\n')
                                        continue
                                    elif nome.replace(" ", "").isalpha():
                                        lista.append(nome)
                                        print('✅ Usuário adicionado!')
                                        break
                        except ValueError:
                            print('[❌ERRO]!\nTente novamente.')
                            continue
                if novo_participante == novo_n:
                    break

        if decisao == 2:
            print(f'Você escolheu a opção ({decisao})!')
            print("\nCarregando", end="", flush=True)
            for _ in range(3):
                time.sleep(1)
                print(".", end="", flush=True)
            time.sleep(1)
            print('\nSucesso!\n')
            time.sleep(1)
            print('='*89)
            print('Lista de participantes inscritos: ')
            for p in range(0, len(lista)):
                print(f'{p + 1} - {lista[p]}')
            print('='*89)
            print('1 - Voltar para o menu')
            print('0 - Encerrar o programa')
            print('='*89)

            while True:
                try:
                    valor_encerrar1 = 0
                    valor_encerrar2 = 1
                    menu_ou_encerrar = int(
                        # Opciona o usuário a decidir se vai continuar com a manipulação
                        input('Digite em qual opção deseja seguir: '))
                    # de listas ou se encerrar o programa.
                    if menu_ou_encerrar == 1:
                        print(f'Opção N° ({menu_ou_encerrar}) escolhida.')
                        print('Voltando para o menu\n')
                        print("Carregando", end="", flush=True)
                        for _ in range(3):
                            time.sleep(1)
                            print(".", end="", flush=True)
                        time.sleep(1)
                        print('\nSucesso!\n')
                        time.sleep(0.5)
                        MI()
                        break
                    if menu_ou_encerrar == valor_encerrar1:
                        break
                    if menu_ou_encerrar != valor_encerrar2 or menu_ou_encerrar != valor_encerrar1:
                        print('[❌ERRO]! Somente [0 ou 1]!')
                        continue

                except ValueError:
                    print('[❌ERRO]! Tente novamente.\n')
                    continue

            if menu_ou_encerrar == valor_encerrar1:
                print(f'Opção N° ({menu_ou_encerrar}) escolhida.')
                print("\nEncerrando o sistema\naguarde alguns segundos",
                      end="", flush=True)
                for _ in range(3):
                    time.sleep(1)
                    print(".", end="", flush=True)
                time.sleep(1)
                print('\n\nPrograma encerrado.')
                decisao == False
                break

        if decisao == 3:
            print(f'Você escolheu a opção ({decisao})!\n')
            print("Carregando", end="", flush=True)
            for _ in range(3):
                time.sleep(1)
                print(".", end="", flush=True)
            time.sleep(1)
            print('\nSucesso!\n')
            print('='*89)
            print('Lista de participantes inscritos: ')
            for p in range(0, len(lista)):
                print(f'{p + 1} - {lista[p]}')
            print('='*89)
            while True:
                primeiro = 0
                ultimo = len(lista) - 1
                try:
                    mudar = int(input(
                        f'Digite o índice que deseja alterar dentre [{primeiro + 1} e {ultimo + 1}]: '))
                    # PAREI AQUI, CONTINUAR NA MANUTENÇÃO DE INDICE INCOERÊNNTE COM O OBJETO ESPECIFICO DA LSITA.
                    indice_humano = mudar - 1
                    if 0 <= indice_humano < len(lista):
                        print(f'❌ O usuário ({lista[mudar]}) foi removido!')
                        while True:
                            alterar = str(
                                input('\nQual o novo nome: ')).title()
                            if re.findall(r'[^a-zA-Zà-úÀ-Ú\s]', alterar) or alterar == '' or not alterar.strip():
                                print('Digite um nome!')
                                continue
                            else:
                                lista.pop(mudar)
                                lista.insert(mudar, alterar)
                                print('✅ Lista atualizada com sucesso!\n')
                                print('='*89)
                                print('Sua lista atual está assim:')
                                for p in range(0, len(lista)):
                                    print(f'{p + 1} - {lista[p]}')

                            print('='*89)
                            print('1 - Voltar para o menu')
                            print('0 - Encerrar o programa')
                            print('='*89)
                            break

                    elif mudar < 0 or mudar >= len(lista):
                        print(
                            '[❌ERRO]! Esta posição está vazia\nTente novamente.\n')
                        continue

                    valor_encerrar1 = 0
                    valor_encerrar2 = 1
                    menu_ou_encerrar = int(
                        input('Digite em qual opção deseja seguir: '))

                    if menu_ou_encerrar == valor_encerrar2:
                        print(f'Opção N° ({menu_ou_encerrar}) escolhida.')
                        print('Voltando para o menu.')
                        print("\nCarregando", end="", flush=True)
                        for _ in range(3):
                            time.sleep(1)
                            print(".", end="", flush=True)
                        time.sleep(1)
                        print('\nPronto!\n')
                        time.sleep(0.5)
                        MI()
                        break
                    if menu_ou_encerrar == valor_encerrar1:
                        break

                    if menu_ou_encerrar != valor_encerrar2 or menu_ou_encerrar != valor_encerrar1:
                        print('[❌ERRO]! Somente [0 ou 1]!')
                        continue

                except ValueError:
                    print('[❌ERRO]! Algo está incorreto.')
                    continue

            if menu_ou_encerrar == 0:
                print(f'Opção N° ({menu_ou_encerrar}) escolhida.')
                print("\nEncerrando o sistema\naguarde alguns segundos",
                      end="", flush=True)
                for _ in range(3):
                    time.sleep(1)
                    print(".", end="", flush=True)
                time.sleep(1)
                print('\n\nPrograma encerrado.')
                decisao == False
                break

        if decisao == 4:
            print(f'Você escolheu a opção ({decisao})!')
            print("\nCarregando", end="", flush=True)
            for _ in range(3):
                time.sleep(1)
                print(".", end="", flush=True)
            time.sleep(1)
            print('\nSucesso!\n')
            print('='*89)
            print('Lista de participantes inscritos: ')
            for p in range(0, len(lista)):
                print(f'{p + 1} - {lista[p]}')
            print('='*89)
            while True:
                primeiro = 0
                ultimo = len(lista) - 1
                try:
                    remover = int(input(
                        f'Digite o índice de quem deseja remover dentre [{primeiro} e {ultimo}]: '))
                    if remover < 0 or remover >= len(lista):
                        print(
                            '[❌ERRO]! Esta posição está vazia\nTente novamente.\n')
                        continue

                    elif 0 <= remover < len(lista):
                        print(
                            f'✅ O Participante ({lista[remover]}) foi removido com sucesso!\n')
                        lista.pop(remover)
                        print('='*89)
                        print('Sua lista atual está assim:')
                        for p in range(0, len(lista)):
                            print(f'{p + 1} - {lista[p]}')
                        print('='*89)
                        print('2 - Remover mais alguém')
                        print('1 - Voltar para o menu')
                        print('0 - Encerrar o programa')
                        print('='*89)

                    valor_encerrar1 = 0
                    valor_encerrar2 = 1
                    valor_encerrar3 = 2
                    while True:
                        try:
                            menu_ou_encerrar = int(
                                input('Digite em qual opção deseja seguir: '))
                            if menu_ou_encerrar == 2:
                                if lista == []:
                                    print(
                                        '[❌ERRO]! A lista já está vazia.\nVolte ao menu ou encerre o programa.\n')
                                    continue
                                else:
                                    print(
                                        f'Opção N° ({menu_ou_encerrar}) escolhida.')
                                    print('✅ Vamos remover mais alguém.\n')
                                    print('='*89)
                                    print('Sua lista atual está assim:')
                                    for p in range(0, len(lista)):
                                        print(f'{p + 1} - {lista[p]}')
                                    print('='*89)
                                    break
                            if menu_ou_encerrar == 1:
                                print(
                                    f'Opção N° ({menu_ou_encerrar}) escolhida.')
                                print('Voltando para o menu...\n')
                                print("Carregando", end="", flush=True)
                                for _ in range(3):
                                    time.sleep(1)
                                    print(".", end="", flush=True)
                                time.sleep(1)
                                print('\nPronto!\n')
                                time.sleep(0.5)
                                MI()
                                break
                            if menu_ou_encerrar == valor_encerrar1:
                                break
                            if menu_ou_encerrar != valor_encerrar2 or menu_ou_encerrar != valor_encerrar1 or menu_ou_encerrar != valor_encerrar3:
                                print('[❌ERRO]! Somente [0, 1 ou 2]!\n')
                                print('='*89)
                                print('2 - Remover mais alguém')
                                print('1 - Voltar para o menu')
                                print('0 - Encerrar o programa')
                                print('='*89)
                                continue
                        except ValueError:
                            print('[❌ERRO]! Somente [0 ou 1]!.\n')
                            print('='*89)
                            print('2 - Remover mais alguém')
                            print('1 - Voltar para o menu')
                            print('0 - Encerrar o programa')

                            print('='*89)
                            continue
                    if menu_ou_encerrar == valor_encerrar1:
                        break
                    if menu_ou_encerrar == valor_encerrar2:
                        break
                except ValueError:
                    print('[❌ERRO]! Algo está incorreto.\n')
                    continue
            if menu_ou_encerrar == 0:
                print(f'Opção N° ({menu_ou_encerrar}) escolhida.')
                print("\nEncerrando o sistema\naguarde alguns segundos",
                      end="", flush=True)
                for _ in range(3):
                    time.sleep(1)
                    print(".", end="", flush=True)
                time.sleep(1)
                print('\n\nPrograma encerrado.')
                decisao == False
                break
        if decisao == 0:
            while True:
                try:
                    certeza = str(
                        input('Deseja encerrar o sistema [S/N]? ')).lower()
                    if certeza == 's':
                        print(f'Você escolheu a opção ({certeza.upper()})!')
                        print(
                            "\nEncerrando o sistema\naguarde alguns segundos", end="", flush=True)
                        for _ in range(3):
                            time.sleep(1)
                            print(".", end="", flush=True)
                        time.sleep(1)
                        print('\n\nPrograma encerrado.')
                        break
                    elif certeza == 'n':
                        print(f'Você escolheu a opção ({certeza.upper()})!')
                        print('Voltando para o menu.\n')
                        print("Carregando", end="", flush=True)
                        for _ in range(3):
                            time.sleep(1)
                            print(".", end="", flush=True)
                        time.sleep(1)
                        print('\nPronto!\n')
                        time.sleep(0.5)
                        MI()
                        break
                    else:
                        print('[❌ERRO]! Somente [S/N].\n')
                        continue
                except ValueError:
                    print('Algo está incorreto.\nTente novamente.')
                    continue
            if certeza == 's':
                break
    except ValueError:
        print('[❌ERRO]! Escolha uma opção dentre as apresentadas!\n')
        continue
