# 1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.
c = 0
while c <= 1000:
    print(c)
    c = c + 1

# # 2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.
nomes = []

while len(nomes) < 10:
    nome = input(f'Digite o nome da {len(nomes) + 1}ª pessoa: ')
    nomes.append(nome)

print('---Lista de Nomes---')
print(nomes)

# Crie um sistema de notas alunos, com as seguintes operações: Utilize While ou for 
print('Sistema de Notas')

for i in range(3):
    senha = input('Senha: ')
    if senha == '123':
        print('Seja bem vindo!')
        notas = []
        p = input('Digite Sim para cadastro das notas ')
        while p == 'Sim':
            nota = float(input(f'Digite a nota {len(notas) + 1}: '))
            notas.append(nota)
            media = sum(notas) / len(notas)
            p = input('Deseja continuar? ')
        else:
            print(media)
            break
else:
    print('Conta Bloqueada.')