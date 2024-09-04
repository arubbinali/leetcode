def romanToInt(s):
    numericals = ["M", "D", "C", "L", "X", "V", "I"]
    values = [1000, 500, 100, 50, 10, 5, 1]
    total = 0
    for _ in s:
        index_of_letter = numericals.index(_)
        value_of_letter = values[index_of_letter]

        if index_of_letter not in [5, 6]:
            index_of_next_letter = index_of_letter + 1
            value_of_next_letter = values[index_of_next_letter]
            
        print(index_of_letter, index_of_next_letter)
        print(value_of_letter, value_of_next_letter)
    

romanToInt("III")