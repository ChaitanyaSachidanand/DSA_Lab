'''Bubble Sort:
- Simple and easy to understand.
- Time complexity: O(n^2) in the worst and average case.
- Space complexity: O(1).
- Not efficient for large datasets.'''
def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)
    return arr

bubble_sort([64, 25, 12, 3, 12,27,2,99,85,22, 11])