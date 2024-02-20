def input_list(limit):
    list=[]
    print("Enter the sorted list")
    for i in range (limit):
        item=int(input(f"enter the item {i} index :"))
        list.append(item)
    return list
def reverse(list):
    rev=[]
    for i in range(len(list)-1,-1,-1):
        rev.append(list[i])
    return rev
list=[]
limit=int(input("Enter the number of element"))
user_list=input_list(limit)
print(user_list)
rev_list=reverse(user_list)
print(rev_list)
