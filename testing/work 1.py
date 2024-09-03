num = int(input("List length:   "))
numbers = [int(input()) for _ in range(num)]
key = int(input("Enter the key element:   "))
for _ in range(len(numbers)):
    if numbers[_] == key:
        print(f"Element found in location {_ + 1}")
        break
