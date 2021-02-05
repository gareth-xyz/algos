
def find_dupe(nums):
    '''
    runtime here is pretty good, but memory saves can be made
    '''
    return len(set(nums)) != len(nums)

    '''
    the below solutions performs better on memory consumption
    '''



if __name__ == '__main__':
    print( find_dupe( [1,2,3,4,5,5,5,5] ) )
