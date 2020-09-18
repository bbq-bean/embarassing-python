# another way to sort a list...

# look at element i and i + 1
# if i is greater than i + 1, swap them
# repeat until list is sorted

sorts = 0
unsorted = T
while unsorted:
    unsorted = Fa
    i = 0
    while i < len(a) - 1:
        if a[i] > a[i + 1]:
            num1 = a[i]
            num2 = a[i + 1]
            a[i] = num2
            a[i + 1] = num1
            sorts = sorts + 1
            unsorted = True
        
        i += 1
