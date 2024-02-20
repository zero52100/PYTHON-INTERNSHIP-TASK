def input_list():
    limit=int(input("Enter the number of element :"))
    list=[]
    print("Enter the sorted list")
    for i in range (limit):
        item=int(input(f"enter the item {i+1} index :"))
        list.append(item)
    return list
def interseaction(list1,list2):
    list=[]
    for i in list1:
        for j in list2:
            if i==j:
             if j not in list:   
                    list.append(j)
    return list

list1=input_list()
list2=input_list()
result=interseaction(list1,list2)
print(result)

