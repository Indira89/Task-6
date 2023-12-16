list1 = [1, 2, 3, 4, 5, 2, 8]
list2 = [5, 6, 7, 8, 9, 7, 2]
list3 = [8, 10, 11, 2, 12, 11, 6]

duplicates = set(list1) & set(list2) & set(list3)

duplicates_list = list(duplicates)

print("Duplicates in the three lists:", duplicates_list)