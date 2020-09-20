# insertion sort
# STARTS from the SECOND element
# for each element(position actually), going FORWARD in the list, compare the VALUE the the VALUE before it
# if the VALUE before it is GREATER, SWAP THE ELEMENTS
# then compare the element swapped to the VALUE behind it again... is it GREATER? SWAP!
# continue until the element before it is LESS, then continue to the NEXT POSITION IN THE LIST
some_list  = [2, 2, 4, 5, 6]

def insertion_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        while unsorted_list[i - 1] > unsorted_list[i] and i > 0:
            unsorted_list[i - 1], unsorted_list[i] = unsorted_list[i], unsorted_list[i - 1]
            i -= 1

    return unsorted_list

print(insertion_sort(some_list.copy()))
