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
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here

# each recurse passes in inclusive 'confines' of a subarray that that recurse should concern itself with
# therefore I need to split, recurse, and sort within these confines
def merge_sort_in_place(arr, l, r):
    # Your code here
    if r - l < 1:
        return

# check that this gets the left middex
    middex = ((r - l) // 2) + l

# check that the confines being recursed are measured correctly for various edge lengths
# theoretically, I should run into cases where either there's 3 left or 2 left
# if there's 2 left I won't recurse on the side without a thing

# left_arr = arr[l] to arr[middex] (inclusive)

    merge_sort_in_place(arr, l, middex) # Sort Left
# right_arr = arr[middex + 1] to arr[r] (inclusive)
    merge_sort_in_place(arr, middex + 1, r) # Sort Right

    # keep track of left_index, right_index in relation to placement from l to middex [left_arr]
    left_index = l
    right_index = middex + 1

    while True:

        if right_index == r + 1:
            break

        if left_index == right_index:
            break

        if arr[left_index] <= arr[right_index]:
            left_index += 1
        else:
            # slice of everything inclusive-exclusive between l and left_index
            # plus shifting right_index

            arr[l:r + 1] = arr[l:left_index] + [arr[right_index]] + arr[left_index:right_index] + arr[right_index+1:r+1]

            right_index += 1
            left_index += 1
        
    return arr

test_merge_in_place = [0, 5, 2, 1, 0, 9, 10, 5, 7, 3, 7]

print(merge_sort_in_place(test_merge_in_place, 0, len(test_merge_in_place) - 1))