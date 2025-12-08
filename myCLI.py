user_name = input("Welcome to this new exciting command line.\nPlease enter your username: ")
print("Hello", user_name)
print("Please enter 'quit' to exit")
print(user_name, "-->", end=" ")

while True:
    user_input = input().strip().lower()
    if user_input == "quit":
        print("Quitting...")
        break
    elif user_input != "":
        print(user_input, "is a nice command")
    else:
        print(user_name, "-->", end=" ")
