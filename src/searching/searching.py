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
    

# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# arr2 = []
# print(binary_search(arr1, -8, 0, len(arr1)-1))
# print(binary_search(arr2, 6, 0, len(arr2)-1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

# get_side assumes that the mid check failed, and that there is at least 2 values left
# output should be a slice of the arr to search or False if the side the value should be on is empty
def get_side(cur_arr, target):
    order = None
    if cur_arr[0] < cur_arr[len(cur_arr)-1]: order = 'asc'
    else: order = 'desc'

    middex = len(cur_arr) // 2

    if target == cur_arr[middex]: return 'wdf???'

    if target > cur_arr[middex]:
        if order == 'asc' and len(cur_arr[middex+1:]): return cur_arr[middex+1:]
        if order == 'desc' and len(cur_arr[:middex]): return cur_arr[:middex]

        return False

    elif target < cur_arr[middex]:
        if order == 'asc' and len(cur_arr[:middex]): return cur_arr[:middex]
        if order == 'desc' and len(cur_arr[middex+1:]): return cur_arr[middex+1:]

        return False


    
def agnostic_binary_search(arr, target):
    # Your code here
    middex = len(arr) // 2
# in any given recurse, if 
    if target == arr[middex]: return True
    if len(arr) == 1: return False

    # in the case that the 1st and last elements equal, the next two possibilities are:
    # 1] none of the items match
    # 2] the items all match
    # if nothing matches, then the proceeding check needs to recognize 
    # that it is eventually not passing anything into recurse

    remainders = get_side(arr, target)
    if not remainders: return -1
    return agnostic_binary_search(remainders, target)

# my_nums = [5, 10, 2, 0, 3, 7, 20, 17, 16, 12]
# search_7 = agnostic_binary_search(my_nums, 7)
# print(search_7)


def iter_agnostic_binary_search(arr, target):
    if not len(arr): return -1

    order = None
    if arr[0] < arr[len(arr) - 1]: order = 1

    elif arr[0] == arr[len(arr) - 1]:
        if target != arr[0]: return -1
        else:return 0

    else: order = 0


    l = 0
    r = len(arr)-1

    midx = r // 2

    while l <= r:
        if target == arr[midx]: return midx

        if target > arr[midx] and order:
            l = midx + 1

        elif target > arr[midx] and not order:
            r = midx - 1

        elif target < arr[midx] and order:
            r = midx - 1

        elif target < arr[midx] and not order:
            l = midx + 1

        midx = ((r - l) // 2 ) + l

    return -1

my_nums = [5, 10, 2, 0, 3, 7, 20, 17, 16, 12]
index_7 = iter_agnostic_binary_search(my_nums, 7)

print(index_7)