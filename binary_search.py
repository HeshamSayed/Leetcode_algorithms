arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# Iterative Binary Search Function

def binary_search(arr, searching_key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        "Best case"
        if arr[mid] == searching_key:
            return mid

        elif arr[mid] < searching_key:
            low = mid + 1
        elif arr[mid] > searching_key:
            high = mid - 1

    return -1



