"""
Working with while control


Boolean verification for looping sentences
"""

# run with while counting:

# variable set (a number value)

num_control = 0

while num_control <= 10:
    print(num_control)
    num_control = num_control+1

# run while string response doesn't match

str_response = ''

while str_response != 'sim':
    str_response = input('Deseja encerrar este bloco? \n')

print('Bloco encerrado.')
