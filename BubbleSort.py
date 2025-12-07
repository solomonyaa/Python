import random

my_list = []
my_list2 = []
LIST_SIZE = 10

def populate_list(list1):
    for i in range(LIST_SIZE):
        random_num = random.randint(-300, 300)
        list1.append(random_num)


def swap_if_larger(list1):
    i = 0
    while i < len(list1) - 1:
        if list1[i] > list1[i + 1]:
            temp = list1[i]
            list1[i] = list1[i + 1]
            list1[i + 1] = temp
        i += 1
    return list1


def bubble_sort(list1):
    i = 0
    while i < len(list1) - 1:
        swap_if_larger(list1)
        i += 1
    return list1


def get_max_index(list1):
    if len(list1) == 0:
        return -1
    elif len(list1) == 1:
        return 0

    i = 1
    max_num = list1[0]
    max_index = 0

    while i < len(list1):
        if list1[i] > max_num:
            max_num = list1[i]
            max_index = i
        i += 1

    return max_index


def move_largest_to_end(list1):
    max_index = get_max_index(list1)
    if max_index < 0 or len(list1) <= 1:
        return

    for i in range(max_index, len(list1) - 1):
        temp = list1[i]
        list1[i] = list1[i + 1]
        list1[i + 1] = temp


populate_list(my_list)
populate_list(my_list2)

print(my_list)
move_largest_to_end(my_list)
print("Largest element moved to the end")
print(my_list, "\n")

print("=" * 70, "\n")

print(my_list2)
bubble_sort(my_list2)
print("List was sorted using bubble sort")
print(my_list2)