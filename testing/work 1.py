# Initializing 1d list
TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

# Output all values to the screen using an iterator
for number in TheData:
    print(number)

# Find if number is in the list `TheData`
def numberFound(num):
    if num in TheData: 
        print("Found")
    else: 
        print("Not found")
    return num in TheData

# Testing the function with values `8` and `9`
print(numberFound(8))
print()
print(numberFound(9))

