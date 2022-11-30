# Extend nested list by adding the sublist

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist=['h','i']   
list1[2][1][2].append(sublist)

print(list1)

