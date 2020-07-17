"""
This is just a simple exercise after environment setup
The following small code demonstrates simple inputs from user and few code PEP8 practices.

TODO: Arrange the remote stations to work with same environment presets
"""

# simple input and variable set

name = input(f'Provide your complete name as parameter: ').title()
print(f'Your given name is: {name}')

genre = input("Escolha o sexo (Masc/Fem/Outro ").upper()


if genre[0] == 'F':
    print(f'Bem vinda {name}!')
elif genre[0] == 'M':
    print(f'Bem vindo {name}!')
else:
    print(f'Olá {name}!')
