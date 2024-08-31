def isPalindrome(x):
 
    first, second_list, reversed_list, final_string = x, [], [], ""

    for _ in range(len(str(x))):
        second_list.append(str(x)[_])

    
    for _ in range(len(second_list) - 1, -1, -1):
        reversed_list.append(second_list[_])

    for _ in reversed_list:
        final_string += _

    second = int(final_string)



    return first == second

print(isPalindrome(23432))