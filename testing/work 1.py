"""

item
LENGTH(myList)
TRUE
found = TRUE
found = FALSE

"""

myList = [4,2,8,17,9,3,7,12,34,21]
item = int(input("Enter number to be found:   "))
found = False
for index in range(len(myList)):
    if item == myList[index]: found = True
if found: print("item found")
else: print("item not found")