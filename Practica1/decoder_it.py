import sys
import time
import matplotlib.pyplot as plt

def help_panel():
    print("Usage: python3 ./decoder_it.py <key> <EX_encoded_text.txt> <EX_decoded_text.txt>")

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


check_args()

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
def decoder(cyphered_text):
    text = ""
    j = 0
    for letter in cyphered_text:
        key_index = j % len(key)  # index of the char from key that will decode the current char of cyphered_text
        if letter in alphabet or letter in alphabet.upper():
            key_char = key[key_index]  # char assigned to the current index
            shift_value = letters[key_char]  # value assigned to the current decoder char
            new_char = alphabet[(letters[letter] - shift_value) % len(alphabet)]  # char to be added
            if letter in alphabet.upper():
                new_char = new_char.upper()
            text += new_char
            j += 1
        else:
            text += letter
    return text


result = decoder(encoded_text)
if result == decoded_text:
    print(result, end=" RESULT: Decoded with exit.")
else:
    print(result)

# Complexity graphic implementation
lengths = [100, 500, 1000, 2000, 5000]
execution_times = []

for length in lengths:
    cyphered_text = encoded_text * length
    start_time = time.time()
    decoder(cyphered_text)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

plt.plot(lengths, execution_times)
plt.xlabel("Input length")
plt.ylabel("Execution time (s)")
plt.title("Complexity")
plt.show()
