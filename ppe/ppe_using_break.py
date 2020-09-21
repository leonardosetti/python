"""

Use of a break into LOOP sentences
"""

# set variable to use in a for with a BREAK (planned stop)

num_control_count = 0

for num_control_count in range(0, 51):
    if num_control_count == 49:
        break
    else:
        print(num_control_count)
print('Broke out!')

decision = ''

while True:
    decision = input('Deseja para o loop? \n').upper()
    if (decision[0] == "Y") or (decision[0] == "S"):
        break
