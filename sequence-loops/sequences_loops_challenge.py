# Input: numbers list
# Output: sum and average of the numbers

print("Sum and Average of the Numbers")

stop = False
list_numbers = []
index=0
sum_numbers=0
average_numbers=0


while not stop:
    x = int(input("Type a number:"))
    list_numbers.insert(index,x)
    index += 1
    stop = int(input("Exit->1 or Continue->0:"))

#for number in list_numbers:
#    print(f"Number {number}")

for number in list_numbers:
    sum_numbers += number

average = sum_numbers/len(list_numbers)

print(f"Sum of numbers:{sum_numbers}")
print(f"Average of the numbers:{average}")
