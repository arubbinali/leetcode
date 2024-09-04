def romanToInt(s):
    numericals = ["M", "D", "C", "L", "X", "V", "I"]
    values = [1000, 500, 100, 50, 10, 5]
    total = 0
    for _ in s:
        print(numericals[_])
    

romanToInt("III")