# Update the first set with items that don’t exist in the second set

set1 = {10, 20, 30}
set2 = {20, 40, 50}

#finding the intersection of the two sets to get the same elements

s3=set1.intersection(set2)

print(s3)

#subtarcting the s3 from the set 1 to get the desired answer

result_set=set1-s3

print(result_set)
