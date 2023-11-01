import random
def quick_sort(arr):
    '''
    Quick Sort:
- Divide-and-conquer algorithm.
- Time complexity: O(n log n) in the average case, O(n^2) in the worst case.
- Space complexity: O(log n) due to recursion.
- Efficient for large datasets and widely used in practice.
'''
    if len(arr)<=1:
        return arr
    print(arr)
    pivot=arr[len(arr)//2]
    print(pivot)
    upper=[x for x in arr if x<pivot]
    print(upper)
    mid=[x for x in arr if x==pivot]
    print(mid)
    lower=[x for x in arr if x>pivot]
    print(lower)
    # print(arr)88888888888888
    return quick_sort(upper)+mid+quick_sort(lower)

print(quick_sort([64, 25, 12, 3, 12,27,2,99,85,22, 11,1]))