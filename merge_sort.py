def merge_sort(items):
    if len(items) == 1:
        return items
    mid = len(items)/2
    left = items[0:mid]
    right = items[mid:]
    merge_sort(left)
    merge_sort(right)
    i, j, k = 0, 0, 0
    while k < len(items):
        if i < len(left) and j < len(right) and (left[i] < right[j]):
            items[k] = left[i]
            i += 1
        elif j < len(right):
            items[k] = right[j]
            j+=1
        else:
            items[k] = left[i]
            i += 1
        k += 1
    return items
