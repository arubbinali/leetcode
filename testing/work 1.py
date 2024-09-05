def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [8, 5, 3, 6, 2]

bubble_sort(arr)
print(arr)  # Output: [2, 3, 5, 6, 8]