
# quickSort setting pivot as last element
def quickSort_last(arr):
    # empty arr catch-case
    if not len(arr):
        return []

    p1v0t = arr[-1]

    less_than = []
    greater_than = []

    for i in arr[:-1]:
        if i >= p1v0t:
            greater_than += [i]
        else:
            less_than += [i]

    if len(less_than):
        less_than = quickSort_last(less_than)

    if len(greater_than):
        greater_than = quickSort_last(greater_than)

    return less_than + [p1v0t] + greater_than