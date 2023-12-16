def distribute_mangoes(mango_bags, num_students):
    mango_bags.sort()  

    min_difference = float('inf')
    for i in range(len(mango_bags) - num_students + 1):
        max_mangoes = mango_bags[i + num_students - 1]
        min_mangoes = mango_bags[i]
        difference = max_mangoes - min_mangoes

        min_difference = min(min_difference, difference)

    return min_difference

mangoes_in_bags = [10, 5, 22, 37, 8, 15]
num_students_in_class = 3

result = distribute_mangoes(mangoes_in_bags, num_students_in_class)
print("Minimum difference:", result)
