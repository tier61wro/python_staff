arr = [2, 3, 30, 90, 100]
x = 1


# mid = l + h // 2
def bin_search(x, arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        print(f'Step_beg:{left=} {right=} {mid=}')
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
        print(f'Step_end:{left=} {right=} {mid=}')
        print('-------------')
    return -1
print(bin_search(x, arr))
