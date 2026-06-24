# 1 Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.
numero = float(input('Digite seu número: '))

if numero > 0:
    print('Seu número é positivo')
elif numero < 0:
    print('Seu número é negativo')
else:
    print('Seu número é zero')

# 2 Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com base na idade.
idade = float(input('Digite sua idade: '))

if 15 < idade < 18:
    print('Você pode votar! Só se quiser...')
elif idade > 17:
    print('Você é obrigado a votar!')
else:
    print('Você não pode votar.')

# 3 Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
num = float(input('Coloque seu número aqui: '))

if num % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')

# 4 Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo é equilátero, isósceles ou escaleno
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.
a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("O triângulo é Equilátero.")
    elif a == b or a == c or b == c:
        print("O triângulo é Isósceles.")
    else:
        print("O triângulo é Escaleno.")
else:
    print("Os números não formam um triângulo válido.")

# 5 Determine se um número é múltiplo de 5 e 7.
numnum = float(input('Digite aqui seu número: '))

if numnum % 5 == 0:
    print('É um multiplo de 5')
elif numnum % 7 == 0:
    print('É um multiplo de 7')
else:
    print('Não é um multiplo de 5 ou 7')

# 6 Verifique se um número é positivo e maior que 10
nu = float(input('Digite seu número: '))

if nu > 10:
    print('O número é positivo e maior que 10')
elif nu > 0:
    print('O número é positivo e menor que 10')
else:
    print('O número é negativo')

# 7 Verifique se um número é divisível por 3 ou 5.
n = float(input('Digite seu número: '))

if n % 3 == 0:
    print('Seu número é divisível por 3')
elif n % 5 == 0:
    print('Seu número é divisível por 5')
else:
    print('Seu número não é divisível por 3 e nem por 5')