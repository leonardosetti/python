"""
This is just a simple exercise after environment setup
The following small code demonstrates simple inputs from user and few code PEP8 practices.

TODO: Arrange the remote stations to work with same environment presets
"""

# simple input and variable set

name = input(f"Provide your complete name as parameter:\n").title()
print(f"Your given name is: {name}\n")
genre = input("Escolha o sexo (M/F/Outro\n").upper()


if genre[0] == 'F':
    print(f'Bem vinda {name}!')
elif genre[0] == 'M':
    print(f'Bem vindo {name}!')
elif genre[0] == 'O':
    print(f'Olá {name}!')
else:
    print(f"Talvez voce tenha digitado '{genre}` por engano, esta n~ao 'e uma opcao valida." )
