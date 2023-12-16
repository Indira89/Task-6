def find_minimum_element(sorted_list):
    if not sorted_list:
        return None 
    return sorted_list[0]
sorted_numbers = [1, 2, 3, 4, 5, 6, 7]

result = find_minimum_element(sorted_numbers)

if result is not None:
    print("Minimum element:", result)
else:
    print("The list is empty.")
