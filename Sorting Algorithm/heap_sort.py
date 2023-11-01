def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        print("Start",arr)
        heapify(arr, n, i)
    
    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root (max element) with last element
        heapify(arr, i, 0)  # Heapify the reduced heap
        print("last",arr)
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap root with largest element
        print("Swap: ",arr)
        heapify(arr, n, largest)  # Recursively heapify the affected sub-tree

print(heap_sort([64, 0,25, 12, 3, 12,27,2,99,85,22, 11,1,24]))