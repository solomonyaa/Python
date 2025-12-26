from io import StringIO


def read_file(path):
    try:
        with open(path, mode='r', encoding='utf-8') as text_file:
            text_str = text_file.read()
            return text_str
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'")
        return None
    except OSError as e:
        print(f"Error: Cannot open file - {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


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


def get_formatted_dict(dictionary):
    i = 0
    str_builder = StringIO()
    str_builder.write("\n")

    for key, value in dictionary.items():
        if i % 10 == 0 and i != 0:
            str_builder.write("\n")
        str_builder.write(f"{key}: {value}, ")
        i += 1

    return str_builder.getvalue()


def save_and_print(path, text, most_common_word, dictionary):
    report = open(path, 'w', encoding='utf-8')
    start = text.index("Title: ")
    end = text.find("\n", start)
    report.write(text[start:end] + "\n")

    start = text.index("Author: ")
    end = text.find("\n", start)
    report.write(text[start:end] + "\n")

    report.write(f"Chars = {len(text)}, Bytes = {len(text.encode('utf-8'))}\n")
    report.write(f"The most common word is: \"{most_common_word[0]}\" with {most_common_word[1]} occurrences.\n")
    report.write("\nWord-Count Dictionary: ")
    report.write(get_formatted_dict(dictionary))

    report.close()

    with open(path, 'r') as file:
        content = file.read()
        print(content)


def main(path, output_path):
    text_str = read_file(path)
    if not text_str: return

    cleaned_text = clean_text(text_str)
    words_dict = to_dict(cleaned_text)

    if not words_dict:
        print("No words found in the text.")
        return

    most_common = get_max_word(words_dict)
    save_and_print(output_path, text_str, most_common, words_dict)


book_name = "frankenstein.txt"
directory = r"C:\Users\solom\PyCharmMiscProject\\"

book_path = directory + book_name
report_name = "report_" + book_name
report_path = directory + report_name
main(book_path, report_path)
