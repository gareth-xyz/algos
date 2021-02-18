def intersect( nums1, nums2 ):
    bigger = 1 if len(nums1) > len(nums2) else 2
    n      = len(nums2) if bigger == 1 else len(nums1)
        
    for num in (nums1 if bigger == 1 else nums2):
        print(num)

if __name__ == '__main__':
    intersect( [4,9,5], [9,4,9,8,4] )
