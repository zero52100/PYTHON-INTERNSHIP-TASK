def recursive_sum(lst, index):
    if index == len(lst):
        return 0
    else:
        return lst[index] + recursive_sum(lst, index + 1)

def input_list():
    limit=int(input("Enter the number of element :"))
    list=[]
    print("Enter the sorted list")
    for i in range (limit):
        item=int(input(f"enter the item {i+1} index :"))
        list.append(item)
    return list

list1=input_list()
result = recursive_sum(list1, 0)
print(f"The sum of the elements in the list is: {result}")