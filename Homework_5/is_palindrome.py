def is_palindrome(value):
    # if len(value) < 2:
    #     return True

    # if value[0] != value[-1]:
    #     return False

    return is_palindrome(value[1:-1]) # [1,-1)

    # if len(value) < 2:
    #     return True

    # return value[0] == value[-1] and is_palindrome(value[1:-1])


text = input('Enter some text: ')

if is_palindrome(text):
    print('Yes')
else:
    print('No')

# x = lambda text: (
#     True if (
#         len(text) <= 1 or text[0] == text[-1] and x(text[1:-1])
#     ) 
#     else False
# )

# if x('abca'):
#     print('Yes')
# else:
#     print('No')


