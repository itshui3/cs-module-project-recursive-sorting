# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # 2nd Attempt
    if not len(arr):
        return -1

    middex_l = (end - start) // 2 + start

    if target == arr[middex_l]: return middex_l
    if start == end: return False

    if target > arr[middex_l]:
        return binary_search(arr, target, middex_l + 1, end)
    else:
        return binary_search(arr, target, start, middex_l)
    

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
arr2 = []
print(binary_search(arr1, -8, 0, len(arr1)-1))
print(binary_search(arr2, 6, 0, len(arr2)-1))
    # 1st Draft

    # middex = ( len(arr[start:end+1]) // 2 ) + start

    # if arr[middex] == target: return middex
    # if start == end: return -1

    # if len(arr[start:end+1]) == 2:
    #     if arr[start] == target: return start
    #     if arr[end] == target: return end
    #     return False

    # if target < arr[middex]:
    #     return binary_search(arr, target, start, middex-1)
    # else:
    #     return binary_search(arr, target, middex, end)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

