def romanToInt(s):
    numericals = ["M", "D", "C", "L", "X", "V", "I"]
    values = [1000, 500, 100, 50, 10, 5, 1]
    total = 0
    for _ in s:
        index_of_letter = numericals.index(_)
        value_of_letter = values[index_of_letter]

        if index_of_letter > 0:
            index_of_prev_letter = index_of_letter - 1
            value_of_prev_letter = values[index_of_prev_letter]
            
        

        print("current:   ", numericals[index_of_letter], index_of_letter, value_of_letter)
        try: print("prev:      ", numericals[index_of_prev_letter], index_of_prev_letter, value_of_prev_letter, "\n")
        except: print("prev:       no val", "\n")
    

romanToInt("MDCLXVI")