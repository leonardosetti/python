""""
simple num check

Verificar em uma série numérica iterável, quais números são pares ou ímpares
Com input do usuário validar se o número é par ou ímpar
Mostrar os Impares, Pares e Primos

"""
# Scope of global variables:

inp_start_i_num = eval(input(f"Informe o primeiro número da série: \n"))
inp_end_i_num = eval(input(f"Informe o último número da série: \n"))
srl_num = range(inp_start_i_num, inp_end_i_num + 1)

if inp_start_i_num % 2 != 0:
    print(f"O número inicial da série é ímpar: {inp_start_i_num}");
else:
    print(f"O número inicial da série é par: {inp_start_i_num}")

if inp_end_i_num % 2 != 0:
    print(f"O número final da série é ímpar: {inp_end_i_num}")
else:
    print(f"O número final da série é par: {inp_end_i_num}")


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
