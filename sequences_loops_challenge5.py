# Input: Two lists
# Output: Return a message if exists or not common items from lists

print("Common items from Lists")

stop_list1 = False
stop_list2 = False
items_list1 = []
items_list2 = []
index_list1 = 0
index_list2 = 0
items_common_lists = []
found_common_items = False

while not stop_list1:
    x = int(input("Add the element to List 1:"))
    items_list1.insert(index_list1,x)
    index_list1 += 1

    stop_list1 = int(input("Exit->1 or Continue->0"))

while not stop_list2:
    y = int(input("Add the element to List 2:"))
    items_list2.insert(index_list2,y)
    index_list2 += 1
    stop_list2 = int(input("Exit->1 or Continue->0:"))

for item_l1 in items_list1:
    for item_l2 in items_list2:
        if item_l2 == item_l1:
            found_common_items = True

if found_common_items == True:
    print(f"Found common items in both lists")
else:
    print(f"Not found common items in both lists")




