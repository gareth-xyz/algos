'''
binary search can only be performed on sorted data

searching complexity:
    O(log n) time
    O(1) space
'''

def binary_search(arr, low, high, key):
    
    if high >= low:

        mid = low + (high-low) // 2

        # if key at mid
        if arr[mid] == key:
            print('found key')
            return mid

        # if ele smaller than mid, check left subarray
        elif arr[mid] > key:
            return binary_search(arr, low, mid-1, key)

        # if ele greater than mid, check right subarray
        else:
            return binary_search(arr, mid+1, high, key)
    else:
        return -1

if __name__ == '__main__':
    arr = [6,3,4,5,9]
    key=9
    binary_search(arr, 0, len(arr)-1, key)