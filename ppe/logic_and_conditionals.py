""" Exercise for logic and conditionals in Python

TODO:
    1. Refactor the displayable messages, you have used many 'user_name' instances. Itg seems too redundant
    2. Think in implement short code and keep the same flow of logic decision
    3. Review typos
    4. Standardize labels and messages. Set all to PT-Br

All following code uses only IF statements and the Binary and Unary blocks of decision
"""

# Use 'if' statement with binary decision 'AND' and 'OR'

active_state = False
login_state = False

user_name = input(f"Olá, por favor informe seu nome abaixo:\n").title()
user_gender = input(f"Escolha seu sexo (M/F/Outro):\n").upper()

if user_gender[0] == "M":
    print(f"Bem vindo {user_name}!\n")
elif user_gender[0] == "F":
    print(f"Bem vinda {user_name}\n")
elif user_gender[0] == "O":
    print(f"Olá {user_name}\n")
else:
    print(f"Opa! Parece que você digitou '{user_gender}' por engano, infelizmente esta não é uma opção válida.\n")

decision_login = input(f"{user_name}, você deseja realizar o login agora? (Y/N):\n").upper()

if decision_login[0] == "Y":
    login_state = True
    print(f"{user_name}, você realizou o processo de login com sucesso. Vamos ao próximo passo.\n")
elif decision_login[0] == "N":
    print(f"Ora {user_name}, você escolheu '{decision_login}', neste caso o login não foi realizado.\n")
    try_again = input(f"{user_name,}você gostaria de tentar mais uma vez?(Y/N)\n").upper()
    if try_again[0] == "Y":
        decision_login = input(f"{user_name}, você deseja realizar o login? (Y/N):\n").upper()
        if decision_login[0] == "Y":
            login_state = True
            print(f"É isso aí {user_name}, você está logado!\n")
        elif decision_login[0] == "N":
            print(f"Você escolheu a opção {decision_login}, portanto seguiremos ao próximo passso sem logar.\n")
        else:
            print(f"Parece que você digitou '{decision_login}' por engano, infelizmente esta não é uma opção "
                  f"válida.\nVamos ao próximo passo...\n")
    elif try_again[0] == "N":
        print(f"Pois bem {user_name}, você decidiu por não realizar o login agora.\nVamos ao próximo passo...")
    else:
        print(f"Parece que você digitou '{try_again}' por engano, infelizmente esta não é uma opção "
              f"válida.\nVamos ao próximo passo...\n")
else:
    print(f"Parece que você digitou '{decision_login}' por engano, infelizmente esta não é uma opção "
          f"válida.\nVamos ao próximo passo...\n")

decision_activate = input(f"{user_name}, gostaria de ativar seu usuário? (Y/N):\n").upper()

if decision_activate[0] == "Y":
    active_state = True
    print(f"{user_name}, seu usuário foi ativado com sucesso!\n")
elif decision_activate[0] == "N":
    print(f"O usuário '{user_name}' foi ativado com sucesso...")
else:
    print(f"Parece que você digitou '{decision_activate}' por engano, infelizmente esta não é uma opção "
          f"válida.\nEncerrando este processo...\n")

print(f"{user_name}, seu status ao final do processamento é:")
if login_state is True:
    print(f"{user_name} está logado!\n")
else:
    print(f"{user_name} não está logado!\n")

if active_state is True:
    print(f"{user_name} está ativo!\n")
else:
    print(f"{user_name} não está ativo!\n")

if login_state and active_state is True:
    print(f"{user_name}, você não possui pendências neste processo! Está habilitado.\n")
elif login_state or active_state is not True:
    print(f"You still pending in process... checking\n")

if login_state is False:
    print(f"You didn't get in or something went wrong. Try login again\n")
else:
    print(f"Login is OK, no issues here!\n")

if active_state is False:
    print(f"You didn't get activated or something went wrong. Try activate again\n")
else:
    print(f"Activation is OK, no issues here!\n\n")

print(f"Process has been done. For new validation, restart the program\n")

active_state = False
login_state = False
