def is_palindrome(value):
    return value == value[::-1]

    # if value == value[::-1]:
    #     return True
    # else:
    #     return False


# def is_palindrome_another(value):
#     # '122222252222220'
#     for i in range(len(value) // 2):
#         if value[i] != value[-i-1]:
#             return False
#
#     return True


def is_palindrome_another(value):
    # '122222252222220'
    it_is_palindrome = True
    for i in range(len(value) // 2):
        if value[i] != value[-i-1]:
            it_is_palindrome = False
            break

    return it_is_palindrome


text = input('Enter a text: ')

if is_palindrome(text):
    print('Yes')
else:
    print('No')

if is_palindrome_another(text):
    print('Yes')
else:
    print('No')
