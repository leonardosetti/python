"""

working with loop

"""

""""
::Out of Scope:: 

option = input(f"set option here:\n").upper()


if option[0] in ["Y", "S", "O"]:
    print(f"positive")
elif option[0] in ["N"]:
    print(f"negative")
else:
    print(f"YOU'VE BEEN KICKED OUT!")

for item in "geek":
    print(item)
"""
for data_num in range(-1, 10):
    print(data_num + data_num)

name = "leonardo setti".upper()

for index_char, char_name in enumerate(name):
    print(char_name)

for full_name in enumerate(name):
    print(full_name[1], end="'")


def optional_item():
    option = input(f"take your option (Y/N): ").upper()
    if option[0] == "Y":
        print(f"Yes --->{option}")
    else:
        print(f"Not YES --->{option}")

