ticket_number = input('Enter the number of ticket: ')

half = len(ticket_number) // 2
# first_half = 0
# second_half = 0
# first_half = second_half = 0
temp_sum = 0

for i in range(half):
    temp_sum += int(ticket_number[i])

for i in range(half, len(ticket_number)):
    temp_sum -= int(ticket_number[i])

if temp_sum == 0:
    print('Yes')
else:
    print('No')




