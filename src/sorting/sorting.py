# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements

#     # Your code here


#     return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) < 2: return arr

    mid = len(arr) // 2  # mid and onwards makes up 'right' arr
    sorted_left, sorted_right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    left_i, right_i = 0, 0
    sorted_arr = []
    while True:

        if left_i > len(sorted_left) - 1:
            sorted_arr += sorted_right[right_i:]
            right_i = len(sorted_right)
            break

        if right_i > len(sorted_right) - 1:
            sorted_arr += sorted_left[left_i:]
            left_i = len(sorted_left)
            break

        if sorted_left[left_i] < sorted_right[right_i]:
            sorted_arr += [sorted_left[left_i]]
            left_i += 1
        else:
            sorted_arr += [sorted_right[right_i]]
            right_i += 1

    return sorted_arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

