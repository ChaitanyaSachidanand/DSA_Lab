def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    # print("left",left)
    right = merge_sort(arr[mid:])
    # print("right",right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    print("left",left)
    print("right",right)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])

            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    print("Sorted result:",result)
    return result

merge_sort([64, 0,25, 12, 3, 12,27,2,99,85,22, 11,1])