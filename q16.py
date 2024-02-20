def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    
    return merged_list

# Get user input for two sorted lists
list1 = [int(x) for x in input("Enter sorted list 1 (space-separated): ").split()]
list2 = [int(x) for x in input("Enter sorted list 2 (space-separated): ").split()]

# Merge the sorted lists
result = merge_sorted_lists(list1, list2)

# Display the result
print("Merged and Sorted List:", result)
