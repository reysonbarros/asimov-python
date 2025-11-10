# Input: Two lists
# Output: Return all duplicated values from lists.

print("Duplicated values from Lists")

stop_list1 = False
stop_list2 = False
items_list1 = []
items_list2 = []
index_list1 = 0
index_list2 = 0
index_merged_list = 0
merged_list = []
aux_merged_list = []
items_duplicated_list = []

while not stop_list1:
    x = int(input("Add the element to List 1:"))
    items_list1.insert(index_list1,x)
    merged_list.insert(index_merged_list,x)
    index_list1 += 1
    index_merged_list += 1

    stop_list1 = int(input("Exit->1 or Continue->0"))

while not stop_list2:
    y = int(input("Add the element to List 2:"))
    items_list2.insert(index_list2,y)
    merged_list.insert(index_merged_list,y)
    index_list2 += 1
    index_merged_list += 1
    stop_list2 = int(input("Exit->1 or Continue->0:"))


for item in merged_list:
    if item not in aux_merged_list:
        aux_merged_list.append(item)
    else:
        items_duplicated_list.append(item)

print(f"Items from List1:{items_list1}")
print(f"Items from List2:{items_list2}")
print(f"Merged Items from Lists:{merged_list}")
print(f"Duplicated Items from Lists:{items_duplicated_list}")



