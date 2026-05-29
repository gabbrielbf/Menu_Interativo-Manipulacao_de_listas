# def superSoma(num1, num2):
#     total = 0
#     if num2 <= num1:
#         print('O segundo valor não pode ser menor OU igual ao primeiro.\n')
#         return False
#     else:
#         lista_nums = []
#         for i in range(num1, num2+1):
#             lista_nums.append(i)
#         soma_nums = sum(lista_nums)
#         print(f'O resultado do cálculo é: {soma_nums}\n')
#         return soma_nums


# superSoma(num1=int(input('\nDigite o Num1: ')),
#           num2=int(input('Digite o Num2: ')))

def menuInterativo():
    print('='*89)
    print(' Participantes - EVENTO ABC ')
    print('='*89)
    print('1 - Cadastrar participante')
    print('2 - Listar participantes')
    print('3 - Atualizar participante')
    print('4 - Remover participante')
    print('0 - Sair')
    print('='*89)
menuInterativo()

