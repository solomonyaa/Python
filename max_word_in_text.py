from io import StringIO


def clean_text(text):
    text = text.lower()
    str_builder = StringIO()

    for char in text:
        if char.isalpha() or char == "'" or char == '’':
            str_builder.write(char)
        else:
            str_builder.write(" ")

    cleaned = str_builder.getvalue()
    return " ".join(cleaned.split())


def to_dict(text):
    words = text.split()
    word_count_dict = {}

    for word in words:
        if word not in word_count_dict:
            word_count_dict.update({word: 1})
        else:
            word_count_dict[word] += 1

    return dict(sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True))


def get_max_word(sorted_dictionary):
    word = list(sorted_dictionary.keys())[0]
    occurrences = sorted_dictionary[word]
    return word, occurrences


def print_dict(dictionary):
    i = 0
    print()

    for key, value in dictionary.items():
        if i % 10 == 0 and i != 0:
            print()
        print(f"{key}: {value}", sep=" ", end=", ")
        i += 1


def main(path):
    try:
        with open(path, mode='r', encoding='utf-8') as text_file:
            print(type(text_file))
            text_str = text_file.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'")
        return
    except OSError as e:
        print(f"Error: Cannot open file - {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    print(type(text_str))

    print("Chars =", len(text_str))
    print("Bytes =", len(text_str.encode('utf-8')))

    cleaned_text = clean_text(text_str)
    words_dict = to_dict(cleaned_text)

    if not words_dict:
        print("No words found in the text.")
        return

    max_word = get_max_word(words_dict)

    print(f"The most common word is: \"{max_word[0]}\" with {max_word[1]} occurrences.")
    print_dict(words_dict)


book_path = r"C:\Users\Solomon\Desktop\DevSecOps Course\Python\alice_in_wonderland.txt"
main(book_path)

