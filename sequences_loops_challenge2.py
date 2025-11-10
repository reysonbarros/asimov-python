# Input: List numbers
# Output: Max number

print("Max number")

stop = False
list_numbers = []
index=0

while not stop:
    x = int(input("Type a number:"))
    list_numbers.insert(index,x)
    index +=1
    stop = int(input("Exit->1 or Continue->0:"))

#for number in list_numbers:
#    print(f"Number {number}")

max_number = list_numbers[0]

for number in list_numbers:
    if number > max_number:
        max_number = number

print(f"Max number:{max_number}")
