def romanToInt(s = "MCMXCIV"):
    key = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    index = list(key.keys()).index("L") + 1  
    total = 0
    for _ in s:
        total += key[_]
        


    print(total)
romanToInt()