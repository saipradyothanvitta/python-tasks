my_list = [10, 20, 30, 40, 50, 11]

# Reverse the list
my_list.reverse()

# Print the reversed list
print(my_list)



list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find common elements using set intersection
common_elements = list(set(list1) & set(list2))

# Print the common elements
print(common_elements)



original_list = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates by converting to a set, then back to a list
unique_list = list(set(original_list))

# Optionally sort to maintain order
unique_list.sort()

# Print the unique list
print(unique_list)



