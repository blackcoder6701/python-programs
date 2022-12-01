#  Update set1 by adding items from set2, except common items

numbers_1 = {10, 20, 30, 40, 50}

numbers_2 = {30, 40, 50, 60, 70}


numbers_1.symmetric_difference_update(numbers_2)
print(numbers_1)
