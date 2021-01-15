# list comprehensions
# syntax:
# new_list = [do something(or nothing) to n for n in number_list]

# get items from list and put them in another list
letter_list = ['a', 'b', 'c', 'd']
new_list = [b for b in letter_list]

# ['a', 'b', 'c', 'd']
print(new_list)

# add 10 to n for n in number_list
number_list = [1, 2, 3, 4]
newer_list = [n + 10 for n in number_list]

# [11, 12, 13, 14]
print(newer_list)

# create list of lists with 2 elements
list_a = [1, 2, 3]
square_cube_list = [[a**2, a**3] for a in list_a]

# [[1, 1], [4, 8], [9, 27]]
print(square_cube_list)

# flatten a list of lists
flat_sc_list = [y for x in square_cube_list for y in x]

# this works just like a nested loop
# for x in square_cube_list:
#     for y in x:
#         add y to the new list

# [1, 1, 4, 8, 9, 27]
print(flat_sc_list)
