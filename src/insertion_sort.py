def insertion_sort(unsorted):
    for i in range(1, len(unsorted)):
        j = 0
        num = unsorted[i]
        while unsorted[j] < num:
            j += 1
        while(i >= j):
            unsorted[i] = unsorted[i - 1]
            i -= 1
        unsorted[j] = num
    return unsorted


print(insertion_sort([1, 3, 2, 5, 4, 8, 7, 6]))
