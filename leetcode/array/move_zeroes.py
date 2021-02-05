def move_zeroes( nums ):
    if len(nums) <= 1:
            return nums
        
    l = r = 0
    while r < len(nums):
        if nums[r] == 0:
            r += 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
            
            l += 1
            r += 1
            
    return nums
        

if __name__ == '__main__':
    print( move_zeroes( [0,0,1] ) )


