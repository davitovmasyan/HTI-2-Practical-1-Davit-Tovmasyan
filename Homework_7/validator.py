import re
import sys


def validate_email(email):
    exp = r'[a-z0-9]{1}(((\.?[\+\-\w])+[a-z0-9])?)@[a-z0-9]{1}(\.?[\+\-\w])*(\.[a-z]{2,10})'

    return re.fullmatch(exp, email) is not None

    # match = re.fullmatch(exp, email)
    
    # if match:
    #     return True
    # else:
    #     return False


def validate_phone_number(phone_number):
    exp = (
        r'0?(77|55|99|91|98)[ -]?'  # operator code
        '('
            r'(\d{3}[ -]?\d{3})|'   # version 1
            r'(\d{2} \d{2} \d{2})|' # version 2
            r'(\d{2}-\d{2}-\d{2})'  # version 3
        ')'
    )

    return re.fullmatch(exp, phone_number) is not None


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Type one of the following commands.\nemail\nphone_number')
        # print('email')
        # print('phone_number')
    elif len(sys.argv) >= 2:
        command = sys.argv[1]
        if command not in ['email', 'phone_number']:
            print('No such command!')
        elif len(sys.argv) == 2:
            print('No value passed!')
        else:
            value = sys.argv[2]
            commands = {
                'email': validate_email,
                'phone_number': validate_phone_number,
            }

            func = commands[command]
            if func(value):
                print('Yes')
            else:
                print('No')


            # if command == 'email':
            #     if validate_email(value):
            #         print('Yes')
            #     else:
            #         print('No')
            # else:
            #     if validate_phone_number(value):
            #         print('Yes')
            #     else:
            #         print('No')
