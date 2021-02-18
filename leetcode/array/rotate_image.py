# rotate the image 90 degress

def rotate(matrix):
    ''' my submission
    n=len(matrix)
    for i in range(n):
        # n passes through
        # each pass, add a new sub list, moving n elements to correct positions
        temp = []
        for row in matrix[:n]:
            temp.insert(0, row.pop(0) )
        matrix.append(temp)
    for i in range(n):
        matrix.pop(0)
    return matrix
    '''
    # fast submission
    def transpose(matrix):
        # first swap numbers into correct places
        # maximum of n swaps
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                # print('trans: i:{}, j:{}'.format(i,j))
                # print(matrix)
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                # print(matrix)
        return matrix

    def reflect(matrix):
        # now reverse each n sub lists
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                print('reflect: i:{}, j:{}'.format(i,j))
                print(matrix)
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
                print(matrix)
        return matrix

    def reverse(matrix):
        n = len(matrix)
        for i in range(n):
            matrix[i].reverse()
        return matrix

    matrix = transpose(matrix)
    matrix = reverse(matrix)
    return matrix


if __name__ == '__main__':
    print( rotate( [[1,2,3],[4,5,6],[7,8,9]] ) )