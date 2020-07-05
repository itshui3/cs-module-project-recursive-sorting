# pivot always first element implementation
def quick_sort(arr):
    # catch-case logic
    if not len(arr):
        return []
    # initialization logic
    pivot = arr[0]

    less_than = []
    greater_than = []

    for i in arr[1:]:
        if i >= pivot:
            greater_than += [i]
        else:
            less_than += [i]

    if len(less_than) > 1:
        less_than = quick_sort(less_than)
    if len(greater_than) > 1:
        greater_than = quick_sort(greater_than)

    return less_than + [pivot] + greater_than

# unsorted = [5, 1, 0, 2, 10, 7, 2, 3, 8, 12, 17, 4]

# print(quick_sort(unsorted))