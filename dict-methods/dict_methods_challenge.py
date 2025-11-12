# Input: Text
# Output: Number of the vowels
import unicodedata
print("Number of the vowels")

def remove_accent(text):
  return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

vowels = {
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
}

text = input("Type the text:")

for vowel in vowels.keys():
    vowels[vowel] = remove_accent(text.lower()).count(vowel)

for k,v in vowels.items():
    print(f"Total vowel {k}: {v}")
