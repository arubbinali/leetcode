List = [21, 35, 4, 7, 8, 5, 1, 20]

def search(list, key):
    key = int(input("Enter the key element:   "))
    for _ in range(len(list)):
        if list[_] == key:
            print(f"Element found in location {_ + 1}")
            break
    else:
        

