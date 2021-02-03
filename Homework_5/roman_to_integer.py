def roman_to_integer(value):
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    result = 0

    for i in range(len(value)):
        symbol = value[i]
        if i < len(value) - 1 and romans[symbol] < romans[value[i + 1]]:
            result += romans[symbol]
        else:
            result += romans[symbol]

    return result


roman = input('Enter some number in roman: ').upper()

print(roman_to_integer(roman))
