# Sort a tuple of tuples by 2nd item

tuple1=(('c', 11), ('a', 46), ('d', 90), ('b', 37))
tuple2=tuple(sorted(list(tuple1),key=lambda x: x[1]))
print(tuple2)
