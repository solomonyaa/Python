import os


def my_api(func_user_name):
    print("Welcome to this new CLI.\nEnter your commands or 'quit' to quit.")
    os.chdir(r'C:\Users\Solomon\PycharmProjects\PythonProject\sandbox')
    contents = os.listdir('.')

    while True:
        print(func_user_name + "--> ", end="")
        inner_user_input = input().strip().lower()
        if inner_user_input == "quit":
            print("Quitting...")
            break
        elif inner_user_input != "":
            if inner_user_input == "pwd":
                print(os.getcwd())
            elif inner_user_input == "ls":
                print(contents)
            elif inner_user_input.startswith("cat "):
                try:
                    with open(inner_user_input[4:], 'r') as f:
                        content = f.read()
                        print(content)
                except FileNotFoundError:
                    continue
            else:
                print(inner_user_input, "is a nice command")


def main():
    while True:
        user_name = input("Please enter your username: ")
        if user_name != "":
            break
        else:
            continue

    print("Hello", user_name)

    while True:
        print("Please enter 'myapi' to enter the CLI or 'exit' to close this terminal.")
        print(user_name + "@comp> ", end="")
        user_input = input().strip().lower()
        if user_input == "myapi":
            my_api(user_name)
        if user_input == "exit":
            break
        else:
            continue


main()
