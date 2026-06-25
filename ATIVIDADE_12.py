# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.
try:
    numero = int(input('Coloque um número inteiro: '))
    print(f'Você digitou o número {numero} com sucesso!')
except:
    print('Erro: Você digitou um número invalido.')

# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.
try:
    num1 = float(input('Coloque o primeiro número: '))
    num2 = float(input('Coloque o segundo número: '))

    resultado = num1 / num2
    print(f'O resultado da divisão é: {resultado}')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except:
    print('Digite apenas números validos.')

# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).
lista = ['Comida', 'Bebida', 'Jogos', 'Música']
indice = 2

def obter(lista, indice):
    try:
        return lista[indice]
    except:
        return 'Erro: o indíce não existe'

resultado = obter(lista, indice)
print(resultado)