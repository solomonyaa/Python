import random

my_list = []
LIST_SIZE = 10
new_list = []


def populate_list(list1):
    for i in range(LIST_SIZE):
        random_num = random.randint(-100, 100)
        list1.append(random_num)


populate_list(my_list)
print(my_list)

while len(my_list) > 0:
    current_min_index = 0
    for index in range(len(my_list)):
        if my_list[index] < my_list[current_min_index]:
            current_min_index = index

    print(my_list[current_min_index])
    new_list.append(my_list[current_min_index])
    del my_list[current_min_index]
    print(my_list)

print("new sorted list:", new_list)