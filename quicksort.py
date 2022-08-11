import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    cent = random.choice(arr)

    larr = []
    marr = []
    rarr = []
    for num in arr:
        if num < cent:
            larr.append(num)
        elif num == cent:
            marr.append(num)
        elif num > cent:
            rarr.append(num)
    return quicksort(larr) + marr + quicksort(rarr)

print(quicksort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))