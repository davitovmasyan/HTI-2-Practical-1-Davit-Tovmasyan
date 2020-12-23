hint = 'Enter a year (YYYY) or (q) to exit: '

year = input(hint)

while year != 'q':
    year = int(year)

    while year < 1 or year > 2021:
        print('Year is wrong!')
        year = int(input('Enter a year (YYYY): '))

    century = year // 100

    if year % 100 != 0:
        century += 1

    print(century)

    year = input(hint)

# year = int(input('Enter a year(YYYY): '))

# year += 99

# century = year // 100

# print(century)
