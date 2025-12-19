import random
from io import StringIO


def create_enc_key():
    abc = [chr(c) for c in range(ord('a'), ord('z') + 1)]

    shuffled_abc = random.sample(abc, len(abc))

    enc_key = {}

    for i in range(26):
        enc_key.update({abc[i]: shuffled_abc[i]})

    return enc_key


def convert_key(enc_key):
    dec_key = {}

    for key, value in enc_key.items():
        dec_key.update({value: key})

    return dict(sorted(dec_key.items()))


def enc_dec_text(text, key_dict):
    text = text.lower()
    str_builder = StringIO()

    for i in range(len(text)):
        if ord('a') <= ord(text[i]) <= ord('z'):
            str_builder.write(key_dict[text[i]])
        else:
            str_builder.write(text[i])

    return str_builder.getvalue()


def print_key_dict(key_dict):
    for key, value in key_dict.items():
        print(key, "➜", value, end="\t")
        if (ord(key) - 96) % 4 == 0:
            print()

    print("\n" + "=" * 40)


def test_all(text):
    enc_key = create_enc_key()
    encrypted_text = enc_dec_text(text, enc_key)

    dec_key = convert_key(enc_key)
    decrypted_text = enc_dec_text(encrypted_text, dec_key)

    print('Original Text:', text)
    print('Encrypted Text:', encrypted_text)
    print('Decrypted Text:', decrypted_text)
    print("=" * (len(text) + 30))

    print("-- Encryption Key --")
    print_key_dict(enc_key)
    print("-- Decryption Key --")
    print_key_dict(dec_key)


user_text = input("Text to encrypt: ")
if not user_text:
    user_text = "The quick brown fox jumps over the lazy dog"
test_all(user_text)
