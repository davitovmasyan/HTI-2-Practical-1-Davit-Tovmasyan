# def is_password_safe(password):
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#
#     is_safe = False
#
#     for char in password:
#         if char in letters:
#             is_safe = True
#             break
#
#     # if is_safe == False:
#     if not is_safe:
#         return False
#
#     is_safe = False
#
#     letters = letters.upper()
#
#     for char in password:
#         if char in letters:
#             is_safe = True
#             break
#
#     if not is_safe:
#         return False
#
#     # digits = ''.join([str(num) for num in range(0, 10)])
#     digits = '0123456789'
#
#     is_safe = False
#
#     for char in password:
#         if char in digits:
#             is_safe = True
#             break
#
#     if not is_safe:
#         return False
#
#     # return len(password) >= 6 and len(password) <= 16
#     return 6 <= len(password) <= 16


def has_symbol(value, symbols):
    has = False

    for char in value:
        if char in symbols:
            has = True
            break

    return has


# def is_password_safe(password):
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#
#     if not has_symbol(password, letters):
#         return False
#
#     if not has_symbol(password, letters.upper()):
#         return False
#
#     # digits = ''.join([str(num) for num in range(0, 10)])
#     digits = '0123456789'
#
#     if not has_symbol(password, digits):
#         return False
#
#     if not has_symbol(password, '$#@'):
#         return False
#
#     # return len(password) >= 6 and len(password) <= 16
#     return 6 <= len(password) <= 16


def is_password_safe(password):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'

    symbol_list = [
        letters,
        letters.upper(),
        digits,
        '$#@',
    ]

    for symbol in symbol_list:
        if not has_symbol(password, symbol):
            return False

    # return len(password) >= 6 and len(password) <= 16
    return 6 <= len(password) <= 16


if is_password_safe(input('Enter your password: ')):
    print('Yes')
else:
    print('No')


# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
