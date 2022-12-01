# Remove items from set1 that are not common to both set1 and set2


numbers_1 = {10, 20, 30, 40, 50}

numbers_2 = {30, 40, 50, 60, 70}

numbers_1.intersection_update(numbers_2)


print(numbers_1)