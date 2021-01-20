heights = [int(num) for num in input('Enter some numbers: ').split()]

stool_sum = 0

max_height = max(heights)

for height in heights:
    stool_sum += max_height - height

print(stool_sum)
