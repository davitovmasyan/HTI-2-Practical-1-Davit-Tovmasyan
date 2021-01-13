numbers = input('Enter numbers: ').split(' ')

# won't work
# for num in numbers:
#     num = int(num)
#     print(num)

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

product = numbers[0] * numbers[1]

for i in range(1, len(numbers) - 1):
    current_product = numbers[i] * numbers[i + 1]
    if current_product > product:
        product = current_product

print(product)
