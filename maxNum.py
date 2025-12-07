list1 = [552, -51, 23, 42, 137, -117, 213, -3, 74, 0]

highest = float('-inf')
second = float('-inf')

for num in list1:
    if num > highest:
        second = highest
        highest = num
    elif num > second and num != highest:
        second = num

print('highest is:', highest)
print('second highest is:', second)

