def input_list():
    limit=int(input("Enter the number of element"))
    list=[]
    print("Enter the sorted list")
    for i in range (limit):
        item=int(input(f"enter the item {i} index :"))
        list.append(item)
    return list
def to_check(list,item_search):
    count=0
    for item in list:
        if item==item_search:
            count += 1
    return count

user_list=input_list()
print(user_list)
item=int(input("Enter the item to check occurance"))
result=to_check(user_list,item)

if(result==0):
    print("Number is not in list")
else:
    print(result)