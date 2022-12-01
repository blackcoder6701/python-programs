# Add a list of elements to a set

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]


#converting the list into the set

color_set_new=set(sample_list)
print(color_set_new)

#merging the sets 

merge_set=sample_set.union(color_set_new)
print(merge_set)
