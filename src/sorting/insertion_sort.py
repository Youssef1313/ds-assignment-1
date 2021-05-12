def insertion_sort(unsorted):
    for i in range(1, len(unsorted)):
        hole = i
        key = unsorted[i]

        while hole > 0 and unsorted[hole - 1] > key:
            unsorted[hole] = unsorted[hole - 1]
            hole -= 1

        unsorted[hole] = key


list = [1, 3, 2, 5, 4, 8, 7, 6]
insertion_sort(list)
print(list)
