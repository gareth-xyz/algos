# This class doesn't really make sense in Python
# since the list data type is pretty much the same
# however, we can use ctypes to get a raw array
import ctypes

class DynamicArray:
    def __init__(self):
        self.array = self.make_array(self.capacity)
        self.len = 0
        self.capacity = 1

    def __len__(self):
        return self.len

    def __getitem__(self,k):
        if not 0 <= k < self.len:
            return IndexError('k is out of bounds !')

    def append(self, item):
        if self.len == self.capacity:
            self._resize(2 * self.capacity)
        
        self.array[self.len] = item
        self.len += 1

    def insertAt(self, item, index):
        if index<0 or index>self.len:
            print('please enter a valid index, len: {}'.format(self.len))
            return

        if self.len == self.capacity:
            self._resize(2 * self.capacity)

        for i in range(self.len-1, index-1,-1):
            # shifts all elements from desired index and beyond by 1
            # [5,6,7,8, None, None, None, None]
            # [None, 5,6,7,8, None, None, None]
            self.array[i+1] = self.array[i]

        self.array[index] = item
        self.len+=1

    def delete(self):
        if self.len==0:
            print('array is empty, del not possible')
            return
        # should this be None, instead of 0?
        self.array[self.len-1]=0
        self.len-=1

    def removeAt(self, index):
        if self.len==0:
            print('array is empty, deletion not possible')
            return

        if index < 0 or index >= self.len:
            return IndexError('Index out of bounds, deletion not possible')

        if index == self.len-1:
            self.array[index]=0
            self.len -= 1
            return
        
        for i in range(index, self.len-1):
            # shifts all elements after deleted index back 1
            # [5,6,7,8, None, None, None, None] len == 8
            # [6,7,8, None, None, None, None, None] len == 8
            self.array[i]=self.array[i+1]

        self.array[self.len-1] = 0
        self.len-=1

    def _resize(self, new_cap):
        B = self.make_array(new_cap) # New bigger array 
          
        for k in range(self.n): # Reference all existing values 
            B[k] = self.A[k] 
              
        self.array = B # Call A the new bigger array 
        self.capacity = new_cap # Reset the capacity

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()