# sort the list

some_list = [5, 2, 7, 3, 8, 10, 8, 11, 12, 4]

# find the lowest element in the list
# append it as the first element of a new list
# remove it from the list we are looping through
# until all the numbers are gone from the list to sort
some_sorted_list = []

while some_list:
    print("at start of loop\n--------")
    lowest = some_list[0]
    print("some_sorted_list: " + str(some_sorted_list))
    print("some_list: " + str(some_list))
    print("lowest: " + str(lowest))
    print()
    print("lowest set to some_list[0], its " + str(lowest))
    print()
    print("comparing lowest to every line in some_list")
    for line in some_list:
        print("is " + str(line) + " lower than " + str(lowest) + "?")
        if line < lowest:
            print("yes")
            lowest = line
            print("then the new lowest is now " + str(lowest))
        else:
            print("no")

    print()
    print("modifying lists...")
    some_list.remove(lowest)
    some_sorted_list.append(lowest)
    print("at start of loop\n--------")
    print("some_sorted_list: " + str(some_sorted_list))
    print("some_list: " + str(some_list))
    print("ending this run of the loop")

print(some_sorted_list)
