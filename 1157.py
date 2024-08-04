input_string = input()

unique_items = {}
for i in input_string.casefold():
    if i not in unique_items:
        unique_items[i] = 1
    else:
        unique_items[i] = unique_items[i] + 1

print(unique_items)

max = 0        
max_item = ''
second_item = 0

for item in unique_items.keys():
    if unique_items[item] > max:
        max = unique_items[item]
        max_item = item
    elif unique_items[item] == max:
        max_item = item
        second_item = item

if max_item == second_item:
    print("?")
else:
    print(max_item.upper())
