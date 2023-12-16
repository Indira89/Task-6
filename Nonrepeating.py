def first_non_repeating_element(nums):
    frequency_dict = {}

    for num in nums:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1

    for num in nums:
        if frequency_dict[num] == 1:
            return num

    return None

numbers = [3, 5, 2, 5, 7, 3, 8, 2]
result = first_non_repeating_element(numbers)

if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found.")
