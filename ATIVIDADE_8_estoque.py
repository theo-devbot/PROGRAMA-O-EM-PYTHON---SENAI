estoque = {
    'Livros':{  
                'livro 1': 10.0, 
                'livro 2': 20.55, 
                'livro 3': 50.60
              },
    'Tablets': {    
                    't1': 500.50, 
                    't2': 250.90, 
                    't3': 470.30
                },
    'Fones': {
                'fone 1': 126.50, 
                'fone 2': 450.0, 
                'fone 3': 155.60
                }
}

carrinho = []
total = []

sec = input(f'seção:{estoque.keys()}: ')
print('Você acessou a seção: ', estoque[sec])
prod = input(f'Escolha o produto: ')
print('Adicionar ao carrinho: ', prod)
carrinho.append(prod)
total.append(estoque[sec] [prod])

sec = input(f'seção:{estoque.keys()}: ')
print('Você acessou a seção: ', estoque[sec])
prod = input(f'Escolha o produto: ')
print('Adicionar ao carrinho: ', prod)
carrinho.append(prod)
total.append(estoque[sec] [prod])

soma = sum(total)
print('R$', soma)
print(carrinho)
lista = ['', '1- Pix', '2- CC', '3- CD']
pag = int(input(f'Escolha a forma de pagamento: {lista[1:]}'))
print('Sua forma de pagamento é:', lista[pag])
print('Obrigado volte sempre!')

input('Digite enter para sair...')