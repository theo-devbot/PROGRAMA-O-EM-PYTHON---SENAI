dados = {}

nome1 = input('Nome')
idade1 = input('Idade')
senha1 = input('Senha')

nome2 = input('Nome')
idade2 = input('Idade')
senha2 = input('Senha')

nome3 = input('Nome')
idade3 = input('Idade')
senha3 = input('Senha')

dados['nomes'] = [nome1, nome2, nome3]
dados['idades'] = [idade1, idade2, idade3]
dados['senhas'] = [senha1, senha2, senha3]

print(dados)

print('Login no sistema.')

login = input('Digite seu nome: ')
senha_acesso = input('Digite sua senha: ')

if login in dados['nomes'] and senha_acesso in dados['senhas']:
    print('Bem vindo ao sistema!')
else:
    print('Cadastro errado!')