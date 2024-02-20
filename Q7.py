def input_list(limit):
    list=[]
    print("Enter the sorted list")
    for i in range (limit):
        item=int(input("enter the item :"))
        list.append(item)
    return list

def binary_search(list,search):
    low,high=0,len(list)-1

    while low<=high:
        mid=(low+high)//2
        mid_value=list[mid]
        if mid_value==search:
            return mid
        elif mid_value<search:
            low=mid+1
        else:
            high=mid-1
    return -1


list=[]
limit=int(input("Enter the number of element"))
user_list=input_list(limit)
print(user_list)
search=int(input("Enter the num to search"))
result=binary_search(user_list,search)
if result!=-1:
    print(f"Target {search} found at index {result}.")
else:
    print("Element not fount")