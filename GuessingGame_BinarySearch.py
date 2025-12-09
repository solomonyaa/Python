# Binary Search
# O(log n) time complexity -> log2(100) = 6.6438 -> 6 or 7 questions to guess

print("Welcome to the Guessing Game.")
print("Please pick a number between 0 (included) and 100 (excluded).")

minNum = 0
maxNum = 100

while True:
    middle = (minNum + maxNum) // 2

    if minNum + 1 >= maxNum:
        print("Your number is:", middle)
        break

    response = input(f"Is it greater than or equal to {middle}? ").strip().lower()

    if response.startswith('y'):
        minNum = middle
    elif response.startswith('n'):
        maxNum = middle
    else:
        continue

