# bubble sort
# what is it good for?
# nothing, its just taught as an introduction to algorithms
some_list  = [6, 2, 5, 4, 2]

unsorted = True

while unsorted:
    unsorted = False
    i = 0

    while i < len(some_list) - 1:
        if some_list[i] > some_list[i + 1]:
            some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
            unsorted = True
        i += 1

print(some_list)
