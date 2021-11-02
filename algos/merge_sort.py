
def merge_sort(arr, left_idx, right_idx):
    
    if left_idx >= right_idx:
        return

    mid = (left_idx+right_idx)//2
    merge_sort(arr, left_idx, mid)
    merge_sort(arr, mid+1, right_idx)
    merge(arr, left_idx, right_idx, mid)

def merge(arr, left_idx, right_idx, mid):
    pass

if __name__ == '__main__':
    arr = [6,3,4,5,9]
    merge_sort(arr)