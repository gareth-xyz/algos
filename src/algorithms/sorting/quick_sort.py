
'''
quick sort is an internal algorithm, faster than merge sort for small data sets

space/time complexity: 
    time
        avg/best: O(n*log n) 
        worst:    O(n^2) - happens if the pivot is in the smaller/upper bound of range
    space
        O(log n) space
'''

def quick_sort(array, low, high):
    if low < high:

        # find pivot such that:
        # elements smaller, are moved to the left
        # elements larger, are moved to the right
        partition_idx = partition(array, low, high)

        # recursive call on the left of pivot
        quick_sort(array, low, partition_idx-1)

        # recursive call on the right of pivot
        quick_sort(array, partition_idx+1, high)

def partition(array, low, high):
    # pivot on rightmost element
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse, compare each element w/ pivot
    for element in range(low,high):
        # if ele is < pivot, swap it with the greater element i
        if array[element] <= pivot:
            i = i+1
            # swap greater element i with element
            (array[i], array[element]) = (array[element], array[i])

    # swap pivot element with greater element i
    (array[i+1], array[high]) = (array[high], array[i+1])

    return i+1

if __name__ == '__main__':
    arr = [6,3,4,5,9]
    print(arr)
    quick_sort(arr, 0, len(arr)-1)
    print(arr)