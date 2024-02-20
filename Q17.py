def input_list():
    limit=int(input("Enter the number of element :"))
    list=[]
    print("Enter the sorted list")
    for i in range (limit):
        item=int(input(f"enter the item {i+1} index :"))
        list.append(item)
    return list
def even_sum(list):
    sum=0
    for i in list:
        if i % 2==0:
            sum+=i
    return sum
list1=input_list()
result=even_sum(list1)

if result==0:
    print("There is not even number in the list")
else:
    print(f"sum of even number ={result}")