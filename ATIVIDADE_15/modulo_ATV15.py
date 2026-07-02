# 1
import random
numero = random.randint(5, 10)

# 2
ramnum = [random.randint(1, 100) for x in range(3)]

# 3
dat = random.choice(range(10, 31))

# 4
def contagem():
    for i in range(10, 0, -1):
        print(i)

    print('Fogo!')

# 5
def pares():
    num = int(input('Coloque o seu número: '))
    soma = 0

    for i in range(2, num + 1, 2):
        soma += i

        print(f"A soma de todos os números pares de 2 até {num} é: {soma}")

# 6
def mul():
    ins = int(input('Número para a tabela: '))
    for i in range(1, 11):
        resultado = ins * i

        print(f'A tabela de multiplicação até dez é {resultado}')

# 7
def imp():
    for pars in range(99, 0, -2):
        print(pars)