# Return a set of elements present in Set A or B, but not both

sample_set1 = {10, 20, 30, 40, 50}

sample_set2 = {30, 40, 50, 60, 70}



result_set=(sample_set1.union(sample_set2))-sample_set1.intersection(sample_set2)

print(result_set)

