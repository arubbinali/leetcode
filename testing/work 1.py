       
#print(linear_search([3, 5, 2, 8, 6], 5))



#bubble sort
def bubble_sort(numbers):
    for _ in range(len(numbers)):
        for __ in range(len(numbers) - _ - 1):
            if numbers[__] > numbers[__ + 1]:
                numbers[__], numbers[__ + 1] = numbers[__ + 1], numbers[__]

    return numbers

def binary_search(unsorted_numbers, number):
    numbers = bubble_sort(unsorted_numbers)
    low, high = 0, len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == number:
            return mid
        elif numbers[mid] > number:
            high = mid - 1
        else:
            low = mid + 1
    return -1
print(binary_search([3, 5, 2, 8, 6], 8))

            


#insertion sort

#linked list ()