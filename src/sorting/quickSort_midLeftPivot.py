
# quick sort with the mid-left element being set as pivot
def quickSort_midLeft(arr):

    if not len(arr):
        return []

    middex = (len(arr) - 1) // 2
    p1v0t = arr[middex]

    less_than = []
    greater_than = []

    for i in arr[:middex]:
        if i >= p1v0t:
            greater_than += [i]
        else:
            less_than += [i]

    for i in arr[middex + 1:]:
        if i >= p1v0t:
            greater_than += [i]
        else:
            less_than += [i]

    less_than = quickSort_midLeft(less_than)
    greater_than = quickSort_midLeft(greater_than)

    return less_than + [p1v0t] + greater_than
