#!usr/bin/python3

def roman_to_int(roman_string):
    rm_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    isAPair = False
    res = 0
    strLen = len(roman_string) - 1
    for i in range(strLen):
        curr = rm_dict[roman_string[i]]
        next = rm_dict[roman_string[i + 1]]
        if isAPair:
            isAPair = False
        elif curr < next and not(isAPair):
            res += next - curr
            isAPair = True
        else:
            res += curr
            if i == strLen - 1:
            res += next
    return res
