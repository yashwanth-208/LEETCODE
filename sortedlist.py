def merge_sorted_lists(list1, list2):
    merged_list = []
    i = 0  # Pointer for list1
    j = 0  # Pointer for list2

    # Merge the two lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append the remaining elements from list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Append the remaining elements from list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


# Define two sorted lists
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

# Merge the two sorted lists
merged = merge_sorted_lists(list1, list2)

# Print the merged list
print(merged)