# Check if two sets have any elements in common. If yes, display the common elements

sample_set1 = {10, 20, 30, 40, 50}

sample_set2 = {60, 70, 80, 90, 10}


if sample_set1.isdisjoint(sample_set2):
    
    print("two sets have nothing in common")


else:
    
    print("two sets have something in common")
    
    result_set = sample_set1.intersection(sample_set2)
    
    print("they have {result_set1} in common".format( result_set1 = result_set ))
    

# result_set = sample_set1.intersection(sample_set2)

# print(result_set)

