#linear search
def linear_search(numbers, number):
    for _ in range(len(numbers)):
        if numbers[_] == number:
            return f"{number} is at index {_} in the list"
    return f"{number} is not in the list"
        
#print(linear_search([3, 5, 2, 8, 6], 1))

