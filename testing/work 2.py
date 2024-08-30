def isPalindrome(x=12321):
    b = [[_ for _ in str(x)][_] for _ in range(len([_ for _ in str(x)])-1, -1, -1)]
    y = "".join(b)
    print(str(x) == str(y), x == y)

    
#isPalindrome()
x = 123
y = 0
while x > 0:
    y = y * 10 + x % 10
    x //= 10
    print(x, y)
#print(y)