#include <stdio.h>

int main() {

    int arr[] = {1,3,5,7,9};

    int n = 5;
    int i = 0;

    // TRAVERSE ARRAY
    printf("Original array elements are :\n");
    for(i = 0; i<n; i++) {
        printf("arr[%d] = %d \n", i, arr[i]);
    }

    // INSERT
    arr[n] = 5;
    printf("New array elements are :\n");
    for(i = 0; i<n; i++) {
        printf("arr[%d] = %d \n", i, arr[i]);
    }
    
}