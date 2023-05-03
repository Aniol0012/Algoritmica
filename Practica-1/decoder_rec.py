import sys

def help_panel():
    print("Usage: python3 ./decoder_rec.py <key> <EX_encoded_text.txt> <EX_decoded_text.txt>")


def check_args():
    try:
        if not sys.argv[1].isalpha():
            raise ValueError()
        elif not sys.argv[2].endswith(".txt") or not sys.argv[3].endswith(".txt"):
            raise ValueError()
        elif len(sys.argv) != 4:
            raise ValueError()
    except ValueError:
        print("Error: Invalid arguments.")
        help_panel()
        sys.exit(1)


key = sys.argv[1]

encoded_text_file = open(sys.argv[2], "r")
encoded_text = encoded_text_file.read()
encoded_text_file.close()

decoded_text_file = open(sys.argv[3], "r")
decoded_text = decoded_text_file.read()
decoded_text_file.close()

alphabet = "abcdefghijklmnopqrstuvwxyz"
letters = {}
for i in range(len(alphabet)):
    char = alphabet[i]
    letters[char] = i
    letters[char.upper()] = i


# O(n) algorithmic cost, depends on parameter length
def decoder(cyphered_text, key, j):
    if not cyphered_text:
        return ""
    letter = cyphered_text[0]
    key_index = j % len(key)  # index of the char from key that will decode the current char of cyphered_text
    if letter in alphabet or letter in alphabet.upper():
        key_char = key[key_index]  # char assigned to the current index
        shift_value = letters[key_char]  # value assigned to the current decoder char
        new_char = alphabet[(letters[letter] - shift_value) % len(alphabet)]  # char to be added
        if letter in alphabet.upper():
            new_char = new_char.upper()
        return new_char + decoder(cyphered_text[1:], key, j + 1)
    else:
        return letter + decoder(cyphered_text[1:], key, j)


result = decoder(encoded_text, key, 0)
if result == decoded_text:
    print(result, end=" RESULT: Decoded with exit.")
else:
    print(result)

# Complexity graphic implementation not done because Python interpreter throws RecursionError. Graphic would be
# the same as iterative version.
