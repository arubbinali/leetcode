#main
class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

#other
class Solution(object):
    def isPalindrome(self, x):
        return int(x) == int("".join([[_ for _ in str(x)][_] for _ in range(len([_ for _ in str(x)])-1, -1, -1)]))
    
class Solution(object):
    def isPalindrome(self, x):
        first, second = x, 0
        while x > 0: second = second * 10 + x % 10; x //= 10
        return first == second