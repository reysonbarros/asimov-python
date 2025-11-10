# Input: List words
# Output: Return all words greater than or equals 5 characters

print("List words")

stop = False
index=0
list_words_gte_5_chars = []

while not stop:
    x = input("Type the word:")
    if len(x) >= 5:
        list_words_gte_5_chars.insert(index,x)
    index += 1
    stop = int(input("Exit->1 or Continue->0:"))

print(f"Words greater than or equals 5 chars:{list_words_gte_5_chars}")
