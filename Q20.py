def input_list():
    limit=int(input("Enter the number of element :"))
    list=[]
    print("Enter the sorted list")
    for i in range (limit):
        item=int(input(f"enter the item {i+1} index :"))
        list.append(item)
    return list
def remve(list,x):
    for i in list:
        if i == x:
            list.remove(i)
        else:
            count=0
            
    return list,count
    

list1=input_list()
element=int(input("Enter the element to remove from the list"))
result,count=remve(list1,element)

if count==0:
    print(f"The element is not in the list {list1}")
else:
    print(f"List after removing the {element} is {result}")