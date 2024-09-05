#bubble sort
def bubble_sort(numbers):
    for _ in range(len(numbers)):
        for __ in range(len(numbers) - _ - 1):
            if numbers[__] > numbers[__ + 1]:
                numbers[__], numbers[__ + 1] = numbers[__ + 1], numbers[__]

    return numbers

#insertion sort
def insertion_sort(numbers):
    for _ in range(1, len(range(numbers))):
        number = numbers[_]
        index_of_prev_number = _ - 1
        while index_of_prev_number >= 0 and number < numbers[index_of_prev_number]:
            numbers[index_of_prev_number + 1] = numbers[index_of_prev_number]
            index_of_prev_number -= 1
        numbers[index_of_prev_number + 1] = number
        
    return numbers

#linear search
def linear_search(numbers, number):
    for _ in range(len(numbers)):
        if numbers[_] == number:
            return f"{number} is at index {_} in the list"
        
    return f"{number} is not in the list"

#binary search
def binary_search(unsorted_numbers, number):
    numbers = bubble_sort(unsorted_numbers)
    low, high = 0, len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == number:
            return f"{number} is at index {mid} in the list"
        elif numbers[mid] > number:
            high = mid - 1
        else:
            low = mid + 1

    return f"{number} is not in the list"

#linked list ()
class Node():
    def __init__(self, element):
        self.element = element
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head:
            last = self.head
            while last.next:
                last = last.next
            print(last.next)
            last.next = new_node
        else:
            self.head - new_node
        
    def display(self):
        current = self.head
        while current:
            print(current.element, end = " ---> ")
            current = current.next
        print("None")

linked_list = LinkedList()
linked_list.append(4)
linked_list.append(9)
linked_list.append(2)
linked_list.append(-19)
linked_list.display()
    