# rotate the array by k steps

def rotate(nums, k):
    ''' my unoptimised submission
    while k > 0:
        nums.insert(0, nums.pop(-1))
        k -= 1
    '''
    '''
    super fast solution
    reverse everything
    then re-reverse each side before/after 

    nums.reverse() # [5, 4, 3, 2, 1]
    nums[0:k] = list(reversed(nums[0:k])) # [ 4, 5 ]
    nums[k:] = list(reversed(nums[k:])) # [ 1, 2, 3 ]
    '''
    # low memory solution
    # nums[:] overwrites object in memory
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]


if __name__ == '__main__':
    rotate( [1,2,3,4,5], 2 )