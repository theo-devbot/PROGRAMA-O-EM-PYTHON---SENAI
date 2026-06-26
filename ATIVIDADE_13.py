#1 CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS
num1 = float(input('Coloque o primeiro número: '))
num2 = float(input('Coloque o segundo número: '))

def comparar(num1, num2):
    status1 = 'par' if num1 % 2 == 0 else 'ímpar'
    status2 = 'par' if num2 % 2 == 0 else 'ímpar'
    print(f'O número {num1} é {status1}')
    print(f'O número {num2} é {status2}')

comparar(num1, num2)
    
#2 CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS
nu1 = float(input('Coloque o primeiro número: '))
nu2 = float(input('Coloque o segundo número: '))
nu3 = float(input('Coloque o terceiro número: '))

def calc(nu1, nu2, nu3):
    multi = nu1 * nu2 * nu3
    print(f'O resultado da multiplicação é {multi}')

calc(nu1, nu2, nu3)

# 3 CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO
base = float(input('Coloque o número base: '))
exponente = float(input('Coloque o número exponente: '))

def potencia(base, exponente):
    calculo = base ** exponente
    print(f'O valor elevado do {base} por {exponente} é {calculo}')

potencia(base, exponente)

# 4 CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS
dig = input('Escreva a sua idade: ')

def especial(dig):
    if dig == '18':
        print('Acho a mensagem secreta!')
    else:
        print('Olá :)')

especial(dig)

# 5 DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA
ano1 = float(input('Ano de seu nascimento: '))
ano_base = 2026

def descobridor(ano1, ano_base):
    conta = ano_base - ano1
    print(f'Sua idade é {conta}.')

descobridor(ano1, ano_base)

# 6 DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999
def verificador_1999(ano, torneio, pais):
    if ano == 1999 and torneio == 'Copa America' and pais == 'Brasil':
        return True
    else:
        return False

resultado = verificador_1999(1999, 'Copa America', 'Brasil')
print(f'O Brasil ganhou o torneio? {resultado}')

# 7  DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE  
# 1 - Função -  cumprimentar o cliente
# 2 - Função - restaurante
# 3 - Sugestão utilize listas  e loops
cardapio = ['Salada', 'Macarronada', 'Sanduiche', 'Sorvete']

def cumprimentar():
    print('Olá! Seja muito bem vindo/a ao restaurante irado!')

def restaurante(menu):
    cumprimentar()
    print('--- Cardapio do Dia! ---')
    
    for i, item in enumerate(menu):
        print(f'{i + 1} - {item}')
    
    while True:
        try:
            escolha = int(input('Digite o número que deseja (ou 0 para sair): '))

            if escolha == 0:
                print('Atendimento Encerrado!')
                break
            elif 1 <= escolha <= len(menu):
                item_escolhido = menu[escolha - 1]
                print(f'Excelente escolha! Seu item {item_escolhido} já está sendo preparado')
                break
            else:
                print('Opção invalida. Por favor escolha um número da lista.')
        except ValueError:
            print('Entrada Invalida. Digite apenas o número correspondente.')

restaurante(cardapio)