'''
Input: number

Output:
Win or Fail
Condition: show hint(greater than or less than) if fail. Maximum fail = 3 times.
'''
import random

print("Secret number")
secret_number = random.randint(1,100)
try_again = True
max_fail = 3
counter_fail = 0
while try_again:
    user_number = int(input("Type the number:"))
    if secret_number == user_number:
        print("You won!")
        try_again = False
        break
    counter_fail = counter_fail + 1
    if counter_fail <= max_fail:
        if user_number > secret_number:
            print(f"Hint{counter_fail}: Secret number is less than {user_number}")
        else:
            print(f"Hint{counter_fail}: Secret number is greater than {user_number}")

    if counter_fail == 3:
        print(f"You lost! The secret number is {secret_number}")
        try_again = False
        break





