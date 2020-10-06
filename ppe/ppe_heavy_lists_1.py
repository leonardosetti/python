"""

Working with lists:

THere is too many ways to deal with lists, here goes some exercise to demonstrate.
"""

# creating simple list of elements:

val_list_a = [1, 3, 3, 3, 44, 2, 9, 0]

n_finder = input(f'Type the number you are searching in the list, if the list contains it, result will display the '
                 f'right indexes positions: ')
n_finder = int(n_finder)
index_control = 0

while index_control < len(val_list_a):
    print(val_list_a.index(n_finder, index_control))
    nxt_id = (val_list_a.index(n_finder, index_control+1))
    index_control = nxt_id + 1
print(f'NEXT_ID = {nxt_id}')
