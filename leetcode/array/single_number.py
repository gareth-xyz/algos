from collections import Counter

def find_single(nums):
    '''
    my slow solution
    
    for i in nums:
        if nums.count(i) == 1:
            return i
    '''

    ''' a lot faster, but uses more memory '''
    counts = Counter(nums)

    for num, count in counts.items():
        if count == 1:
            return num

if __name__ == '__main__':
    print(find_single([1,1,1,2]))
