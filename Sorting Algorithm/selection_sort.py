'''- Bubble Sort and Selection Sort have a time
 complexity of O(n^2) in the worst and
   average case, while Insertion Sort has the same
     time complexity but performs well on nearly 
     sorted data.'''


def selection_sort(arr):
    '''Selection Sort:
- Simple and easy to implement.
- Time complexity: O(n^2) in the worst and average case.
- Space complexity: O(1).
- Not efficient for large datasets.'''
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)#,"\n")
    return arr

selection_sort([64, 25, 12, 3, 12,27,2,99,85,22, 11])