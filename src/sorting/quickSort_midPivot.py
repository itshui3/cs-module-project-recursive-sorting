
# quickSort with middle-right element acting as pivot
def quickSort_mid(arr):
    if not len(arr):
        return []

    middex = len(arr) // 2
    p1v0t = arr[middex]

    less_than = []
    greater_than = []

    # loop left
    for i in arr[:middex]:
        if i >= p1v0t:
            greater_than += [i]
        else:
            less_than += [i]

    # loop right
    for i in arr[middex + 1:]:
        if i >= p1v0t:
            greater_than += [i]
        else:
            less_than += [i]

    less_than = quickSort_mid(less_than)
    greater_than = quickSort_mid(greater_than)

    return less_than + [p1v0t] + greater_than

# if for loop attempts to iterate through empty iterator, what happen?

unsorted = [5, 1, 0, 2, 10, 7, 2, 3, 8, 12, 17, 4]

print(quickSort_mid(unsorted))