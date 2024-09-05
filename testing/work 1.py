def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [3, 5, 2, 8, 6]
print(linear_search(arr, 8))  # Output: 3
