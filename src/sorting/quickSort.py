# pivot always first element implementation
def quick_sort(arr):
    # catch-case logic

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