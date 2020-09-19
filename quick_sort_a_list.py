'''
quick sort:
1)select a value as a pivot point. it can be anything, but its better to get the middle number of whatever the low/mid/hi
values are
2)then start sorting the rest as being higher or lower than the pivot
3)
'''

some_list = [6,4,8,9,44,7]

def quick_sort(unsorted_list):
    # first, is the list even longer than 1 item? doesnt need to be sorted then
    if len(unsorted_list) <= 1:
        return unsorted_list

    # need to find good index for this
    pivot = 0

    # next try to get a good pivot, these are the INDEXES, NOT the low/mid/high VALUES
    low = 0
    high = len(unsorted_list) - 1
    mid = len(unsorted_list) // 2

    # next use the INDEXES to get the VALUES, and sort the VALUES to get the MEDIAN value
    sort_l_m_h = sorted([unsorted_list[low], unsorted_list[mid], unsorted_list[high]])
    median = sort_l_m_h[1]

    # now find the INDEX of the MEDIAN
    if median == unsorted_list[low]:
        pivot = low
    elif median == unsorted_list[mid]:
        pivot = mid
    else:
        pivot = high

    pivot_value = unsorted_list.pop(pivot)

    # now create 2 sides to sort, either higher than pivot or lower...
    lower_side = []
    higher_side = []

    for line in unsorted_list:
        if line > pivot_value:
            higher_side.append(line)
        else:
            lower_side.append(line)

    return quick_sort(lower_side) + [pivot_value] + quick_sort(higher_side)


sort_me_up = quick_sort(some_list.copy())
