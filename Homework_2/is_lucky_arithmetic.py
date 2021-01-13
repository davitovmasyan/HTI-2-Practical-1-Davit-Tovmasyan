def is_lucky(value):
    half = len(value) // 2
    temp_sum = 0
    value = int(value)
    i = 0
    while value != 0:
        digit = value % 10
        if i < half:
            temp_sum += digit
        else:
            temp_sum -= digit

        i = i + 1
        value = value // 10

    return temp_sum == 0
    # if temp_sum == 0:
    #     return True
    # else:
    #     return False


ticket_number = input('Enter the number of ticket: ')

if is_lucky(ticket_number):
    print('Yes')
else:
    print('No')


# print(is_lucky('1230'), '1230')
# print(is_lucky('123090'), '123090')
# print(is_lucky('22'), '22')



