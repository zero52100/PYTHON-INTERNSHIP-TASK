def input_list():
    limit=int(input("Enter the number of element :"))
    list=[]
    print("Enter the sorted list")
    for i in range (limit):
        item=int(input(f"enter the item {i+1} index :"))
        list.append(item)
    return list
def check_duplicate(list):
    new_list=[]
    count=0
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

user_list=input_list()
result=check_duplicate(user_list)

print("List after removing duplicates:",user_list)
print("List after removing duplicates:",result)
