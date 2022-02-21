'''
merge sort is an efficient external algorithm, allowing sorting to be distributed in batches

sorting will always be: 
    O(n*log n) time
    O(n) space - unless we optimise to only take O(1) space
'''

def merge_sort(array):
    if len(array) > 1:

        # split into 2 subarrays
        split_idx = len(array) // 2
        left = array[:split_idx]
        right = array[split_idx:]

        # sort 2 halves
        merge_sort(left)
        merge_sort(right)

        idx_left = idx_right = idx_sorted_arr = 0

        # until we reach end of either left or right
        # place smaller item in the correct sorted array slot
        while idx_left < len(left) and idx_right < len(right):
            if left[idx_left] < right[idx_right]:
                array[idx_sorted_arr] = left[idx_left]
                idx_left += 1
            else:
                array[idx_sorted_arr] = right[idx_right]
                idx_right += 1
            idx_sorted_arr += 1
                

        # when left or right is empty
        # place the remaining items in array
        while idx_left < len(left):
            array[idx_sorted_arr] = left[idx_left]
            idx_left += 1
            idx_sorted_arr += 1

        while idx_right < len(right):
            array[idx_sorted_arr] = right[idx_right]
            idx_right += 1
            idx_sorted_arr += 1
            

if __name__ == '__main__':
    arr = [6,3,4,5,9]
    print(arr)
    merge_sort(arr)
    print(arr)
