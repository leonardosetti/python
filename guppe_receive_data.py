""""
Exercícios de input de dados
"""

nome = input("Qual seu nome ").title()

sexo = input("Escolha o sexo (Masc/Fem/Outro ").upper()


if sexo[0] == 'F':
    print(f'Bem vinda {nome}!')
elif sexo[0] == 'M':
    print(f'Bem vindo {nome}!')
else:
    print(f'Olá {nome}!')


zuer1 = (nome[::-1]).lower()
zuer2 = (nome.split()[1]).upper()
