def input_list():
    limit=int(input("Enter the number of element :"))
    list=[]
    print("Enter the sorted list")
    for i in range (limit):
        item=int(input(f"enter the item {i+1} index :"))
        list.append(item)
    return list
def second_largest(list):
    if len(list)<2:
        return " List should have minimum 2 elemwnt"
    second_largest=float('-inf')
    largest=float('-inf')
    for i in list:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest and i != largest:
            second_largest=i
    return second_largest
list1=input_list()
second=second_largest(list1)
print(second)
