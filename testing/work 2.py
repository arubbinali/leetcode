def isPalindrome(x=12321):
    b = [[_ for _ in str(x)][_] for _ in range(len([_ for _ in str(x)])-1, -1, -1)]
    y = "".join(b)
    print(str(x) == str(y), x == y)

    
#isPalindrome()
x = 123


def isPalindrome(x):
    first, second = x, 0
    while x > 0: second = second * 10 + x % 10; x //= 10
    return first == second

#print(isPalindrome(121))

def l(x):
    return str(x) == str(x)[::-1]

print(l(3314133))