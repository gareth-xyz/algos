'''
selection sort is fairly inefficient but good for small data sets

sorting will always be: 
    O(n^2) time
    O(1) space
'''

def selection_sort(array):
    
    for step in range(len(array)):
        min_idx = step

        for i in range(step + 1, len(array)): 
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

if __name__ == '__main__':
    arr = [6,3,4,5,9]
    print(arr)
    selection_sort(arr)
    print(arr)
