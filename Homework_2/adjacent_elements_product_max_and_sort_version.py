def my_max(items):
    if len(items) == 0:
        return None

    max_element = items[0]
    for num in items:
        if num > max_element:
            max_element = num

    return max_element


# numbers = [int(num) for num in input('Enter numbers: ').split(' ')]
numbers = list(map(int, input('Enter numbers: ').split(' ')))

products = []

for i in range(len(numbers) - 1):
    product = numbers[i] * numbers[i + 1]
    products.append(product)


print(max(products))
# print(my_max(products))
print(sorted(products, reverse=True)[0])

# def sort(items):
#     # 1 9 4 5 2 3 10
#     max_element = items[0]
#     for i in range(len(items)):
#         if items[i] > max_element:
#             items[-1] = items[i]
#             max_element = items[i]
