def min_a(x):
    ''' min in list O(n^2) - compare each number to every other number in the list '''
    res = x[0]
    for i in x:
        for n in x:
            if i < n and i < res:
                min_num = True
            else:
                min_num = False
        if min_num == True:
            res = i
    return res

def min_b(x):
    ''' min in list O(n) - linear growth in s/t complexity '''
    min_num = x[0]
    for i in x:
        if i < min_num:
            min_num=i
    return min_num

if __name__ == "__main__":
    print(min_a([1,2,3,4,5]))
    print(min_b([1,2,3,4,5]))