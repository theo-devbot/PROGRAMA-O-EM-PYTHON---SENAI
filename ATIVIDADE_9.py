print('seja bem vindo ao hotel...')

quantidade_pessoas =  int(input('Quantidade Pessoas: '))

dados  = {}

quartos = ['',"Simples", "Duplo" , "Luxo"]
valores_quartos = [0,100.0,150.0,250.0]

print(f'1 - {quartos[1]}R$ {valores_quartos[1]}')
print(f'2 - {quartos[2]}R$ {valores_quartos[2]}')
print(f'3 - {quartos[3]}R$ {valores_quartos[3]}')


if quantidade_pessoas == 1:
    nome = input('Nome: ')
    idade = input('idade: ')
    dados['nomes'] = [nome]
    dados['idades'] = [idade]

    dia = int(input(f'Quantidade de dias: {nome}'))
    quarto_es =  int(input('Escolha o quarto: '))
    calculo = dia * valores_quartos[quarto_es]
    print('R$ ', calculo)
    forma = input('Digite a forma de pagamento: pix | cc | cd')
    print('obrigada volte sempre!') 


elif quantidade_pessoas == 2:
    nome1 = input('Nome: ')
    idade1 = input('idade: ')    
    nome2 = input('Nome: ')
    idade2 = input('idade: ') 

    dados['nomes'] = [nome1, nome2]
    dados['idades'] = [idade1, idade2]

    dia = int(input(f'Quantidade de dias: {nome1}'))
    quarto_es =  int(input(f'Escolha o quarto: {nome1}'))
    calculo = dia * valores_quartos[quarto_es]
    print('R$ ', calculo)
    forma = input('Digite a forma de pagamento: pix | cc | cd')
    print('**** ' * 10)
    dia = int(input(f'Quantidade de dias:{nome2} '))
    quarto_es =  int(input(f'Escolha o quarto:{nome2} '))
    calculo = dia * valores_quartos[quarto_es]
    print('R$ ', calculo)
    forma = input('Digite a forma de pagamento: pix | cc | cd')
    
    print('obrigada volte sempre!')

elif quantidade_pessoas == 3:
    nome3 = input('Nome: ')
    idade3 = input('idade: ')    
    nome4 = input('Nome: ')
    idade4 = input('idade: ')     
    nome5 = input('Nome: ')
    idade5 = input('idade: ') 
  
    
    dados['nomes'] = [nome3, nome4, nome5]
    dados['idades'] = [idade3, idade4, idade5]
    

    dia = int(input(f'Quantidade de dias: {nome3}'))
    quarto_es =  int(input(f'Escolha o quarto: {nome3}'))
    calculo = dia * valores_quartos[quarto_es]
    print('R$ ', calculo)
    forma = input('Digite a forma de pagamento: pix | cc | cd')

    print('**** ' * 10)

    dia = int(input(f'Quantidade de dias:{nome4} '))
    quarto_es =  int(input(f'Escolha o quarto:{nome4} '))
    calculo = dia * valores_quartos[quarto_es]
    print('R$ ', calculo)
    forma = input('Digite a forma de pagamento: pix | cc | cd')    

    print('**** ' * 10)
    
    dia = int(input(f'Quantidade de dias:{nome5} '))
    quarto_es =  int(input(f'Escolha o quarto:{nome5} '))
    calculo = dia * valores_quartos[quarto_es]
    print('R$ ', calculo)
    forma = input('Digite a forma de pagamento: pix | cc | cd') 

    # print(dados)
    print('obrigada volte sempre!')