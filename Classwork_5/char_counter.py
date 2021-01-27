text = input('Enter a text: ')

count = {}
# count['a'] = 1
# count['a'] += 1
# count['a'] = count['a'] + 1
for char in text:
    # if char in count.keys():
    #     count[char] += 1
    # else:
    #     count[char] = 1

    # count.setdefault(char, 0)
    # count[char] += 1

    count[char] = count.get(char, 0) + 1

print(count)

# for char in text:
#     if char not in count.keys():
#         count[char] = text.count(char)

