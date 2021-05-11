def bubble_sort(unsorted):
    length = len(unsorted)
    for i in range(length):
        madeAnySwaps = False
        for j in range(0, length - i - 1):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                madeAnySwaps = True
        
        if not madeAnySwaps:
            break


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)