def romanToInt(s = "MCMXCIV"):
    key = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    
    total, prev_index = 0, 0
    for _ in s:
        index = list(key.keys()).index(_)
        print(index)
        if index >= prev_index:
            total += key[_]
            print("total: ", total)
        else:
            pass
        prev_index = index
        
        
    print(total)
romanToInt()