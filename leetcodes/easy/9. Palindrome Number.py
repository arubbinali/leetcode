#main
class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

#other
class Solution(object):
    def isPalindrome(self, x):
        first, second = x, 0
        while x > 0: second = second * 10 + x % 10; x //= 10
        return first == second
    
class Solution(object):
    def isPalindrome(self, x):
        first, second_list, reversed_list, final_string = x, [], [], ""

        for _ in range(len(str(x))): second_list.append(str(x)[_])
        for _ in range(len(second_list) - 1, -1, -1): reversed_list.append(second_list[_])
        for _ in reversed_list: final_string += _

        return str(first) == final_string