import random
from io import StringIO


def create_enc_key():
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

    shuffled_abc = random.sample(abc, len(abc))

    enc_key = {}

    for i in range(26):
        enc_key.update({abc[i]: shuffled_abc[i]})

    return enc_key


def convert_key(enc_key):
    dec_keys = list(enc_key.values())
    dec_values = list(enc_key.keys())

    dec_key = {}

    for i in range(26):
        dec_key.update({dec_keys[i]: dec_values[i]})

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
        if ord(key) % 2 == 1:
            print(key, "->", value, end="\t")
        else:
            print(key, "->", value, end="\n")


def test_all(text):
    enc_key = create_enc_key()
    encrypted_text = enc_dec_text(text, enc_key)

    dec_key = convert_key(enc_key)
    decrypted_text = enc_dec_text(encrypted_text, dec_key)

    print('Original Text:', text)
    print('Encrypted Text:', encrypted_text)
    print('Decrypted Text:', decrypted_text)
    print("=" * 50)

    print("-- Encryption Key --")
    print_key_dict(enc_key)
    print("=" * 50)
    print("-- Decryption Key --")
    print_key_dict(dec_key)
    print("=" * 50)


sample_text = "Can you read this?"
test_all(sample_text)
