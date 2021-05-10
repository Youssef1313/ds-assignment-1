import math
def merge_sort(unsorted):
    length = len(unsorted)
    if length <= 1: return unsorted

    if length > 2:
        unsorted_half1, unsorted_half2 = divide(unsorted)
        return merge(merge_sort(unsorted_half1), merge_sort(unsorted_half2))

    #if this line is reached so unsorted length must = 2
    if unsorted[0] > unsorted[1]:
        unsorted[0] , unsorted[1] = unsorted[1] , unsorted[0]
        return unsorted

def divide(unsorted):
    half_i = math.ceil(len(unsorted) / 2)
    return unsorted[:half_i-1], unsorted[half_i-1:]

def merge(sorted_half1, sorted_half2):
    i = 0
    j = 0
    k = 0
    half1_length = len(sorted_half1)
    half2_length = len(sorted_half2)
    _sorted = [0] * (half1_length + half2_length)
    while i!= half1_length and j != half2_length:
        if sorted_half1[i] < sorted_half2[j]:
            _sorted[k] = sorted_half1[i]
            i +=1
        else:
            _sorted[k] = sorted_half2[j]
            j +=1
        k += 1
    
    _sorted[k:] = sorted_half1[i:] if i != half1_length else sorted_half2[j:]
    return _sorted

#test case
print(merge_sort([1, 3, 2]))
