def input_list():
    limit=int(input("Enter the number of element :"))
    list=[]
    print("Enter the sorted list")
    for i in range (limit):
        item=int(input(f"enter the item {i+1} index :"))
        list.append(item)
    return list
def count(tuple_data):
    occurrences = {}
    for element in tuple_data:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1
    return occurrences

list1=input_list()
user_tuple = tuple()
for element in list1:
    user_tuple += (element,)
print(user_tuple)
result = count(user_tuple)
print("Occurrences of each element in the tuple:")
for element, count in result.items():
    print(f"{element}: {count} times")