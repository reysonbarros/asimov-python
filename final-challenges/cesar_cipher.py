# Input: text and key size
# Output: text using Cesar's Cipher

# Samples:
# Input: abc using key size = 1
# Output: bcd

import operator as op

print("Cesar's Cipher")

upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_chars = upper_chars.lower()
cesar_cipher_text = ""

text = input("Type some text:")
key_size = int(input("Type the key size:"))

for char in text:
    if op.contains(upper_chars, char):
        index_char = upper_chars.index(char)
        cesar_cipher_text += upper_chars[index_char + key_size]
    elif op.contains(lower_chars, char):
        index_char = lower_chars.index(char)
        cesar_cipher_text += lower_chars[index_char + key_size]
    else:
        cesar_cipher_text += char


print(cesar_cipher_text)
