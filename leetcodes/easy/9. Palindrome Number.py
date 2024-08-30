#main

#other
class Solution(object):
    def isPalindrome(self, x):
        return int(x) == int("".join([[_ for _ in str(x)][_] for _ in range(len([_ for _ in str(x)])-1, -1, -1)]))