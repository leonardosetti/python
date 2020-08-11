"""
TODO: Determine the best practice for ranges
    1.Use loop and conditional statements
    2.Apply PEP8
    3.Describe the code blocks
"""

"""
# Range style 1
for value in range(20):
    print(value)

# Range style 2
for value in range(0, 10):
    print(value)

# Range style 3
for value in range (3,99,3):
    print(value)

# Range style 4 (!reverse)
for value in range(72, -1, -8):
    print(value)
"""
# Prompt to user which style of range is wanted

usr_choice = input(f"Por favor escolha qual estilo de Range gostaria de usar:\n"
                   f"   \U000021E8 1. Defina apenas o valor de parada.\n"
                   f"   \U000021E8 2. Defina o valor de início e valor de parada.\n"
                   f"   \U000021E8 3. Defina o valor de início, valor de parada e o passo incremental.\n"
                   f"   \U000021E8 4. Defina o valor de início, valor de parada e o passo decremental.\n"
                   f"\U000025B0\U000025B0\U000025B0\U000025B6 ")

# After user take a choice, this block verify and ensures the typed value
if usr_choice not in range(1, 5):
    print(f"infelizmente você digitou um valor diferente do esperado.\n"
          f"Deseja tentar novamente? (S/N")
