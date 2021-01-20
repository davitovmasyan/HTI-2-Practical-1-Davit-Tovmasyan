def get_number_root(input_number):
    string = str(input_number)
    input_numbers_sum = sum([int(i) for i in string])

    if input_numbers_sum < 10:
        return input_numbers_sum
    else:
        # I have some problems here. When the sum is not greater then 10
        return get_number_root(input_numbers_sum)
        # automaticly called else brackets.


num = int(input("Please input number:"))

if num < 0:
    print("Please input not negativ nambers.")
else:
    result = get_number_root(num)
    # If result greater then 10, I get None result.
    print(f"The root number of input value is {result}")
