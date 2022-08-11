def merge_list(a, b):
    c = []
    leng1 = len(a)
    leng2 = len(b)

    i = j = 0
    while i < leng1 and j < leng2:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]    
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_list(left, right)   