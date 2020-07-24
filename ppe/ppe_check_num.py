""""
simple num check

Verificar em uma série numérica iterável, quais números são pares ou ímpares
Com input do usuário validar se o número é par ou ímpar

"""
# Scope of global variables:

inp_start_i_num = eval(input(f"Informe o primeiro número da série: \n"))
inp_end_i_num = eval(input(f"Informe o último número da série: \n"))
srl_num = range(inp_start_i_num, inp_end_i_num + 1)

print("\nSérie completa:")

for data_num in srl_num:
    print(data_num, end=" ")

print("\nÍmpares:")

for data_num in srl_num:
    if data_num % 2 != 0:
        print(data_num, end=" ")

print("\nPares:")

for data_num in srl_num:
    if data_num % 2 == 0:
        print(data_num, end=" ")

print("\nPrimos:")

for data_num in srl_num:
    if data_num > 1:
        for key_num in range(2, data_num):
            if (data_num % key_num) == 0:
                break
        else:
            print(data_num, end=" ")
