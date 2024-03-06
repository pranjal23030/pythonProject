def find_common_elements_with_loops(list1, list2):
    common_elements = []

    # Iterate through each element in list1
    for item1 in list1:
        # Check if the element is also in list2
        if item1 in list2 and item1 not in common_elements:
            common_elements.append(item1)

    return common_elements


# Example usage
a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6, 9, 2, 1, 3, 5]

result = find_common_elements_with_loops(a, b)
print("Common elements (using loops):", result)
