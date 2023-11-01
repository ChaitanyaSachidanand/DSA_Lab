'''Bubble Sort and Selection Sort have a time complexity of O(n^2) in the worst and average case, while Insertion Sort has the same time complexity but performs well on nearly sorted data.'''
def insertion_sort(arr):
    ''' Insertion Sort:
- Efficient for small datasets and partially sorted arrays.
- Time complexity: O(n^2) in the worst and average case.
- Space complexity: O(1).
- Performs well on nearly sorted data.'''
    n=len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
        print(arr)
    return arr
insertion_sort([64, 25, 12, 3, 12,27,2,99,85,22, 11])