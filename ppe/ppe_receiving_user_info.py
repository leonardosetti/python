"""
This is just a simple exercise after environment setup
The following small code demonstrates simple inputs from user and few code PEP8 practices.
"""

# simple input and variable set

# Tratando o input com as iniciais maiúsculas:
name = input(f"Insira seu nome e este programa formatará da maneira correta:\n").title()

# Eliminando possíveis espaços em branco no nome:
name = " ".join(name.split())

# Fornecendo a saída com o nome formatado:
print(f'Seu nome foi definido como: {name}\n')

# Decisão para tratamento de boas vindas:
genre = input("Escolha o sexo (M/F/Outro)\n").upper()

if genre[0] == 'F':
    print(f'Bem vinda {name}!')  # tratamento no feminino
elif genre[0] == 'M':
    print(f'Bem vindo {name}!')  # tratamento no masculino
elif genre[0] == 'O':
    print(f'Olá {name}!')  # tratamento sem gênero definido
else:
    print(f"Talvez você tenha digitado '{genre}` por engano, esta não é uma opção válida.")  # aviso de Typo
