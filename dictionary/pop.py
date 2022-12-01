sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]


result_dict= {k:sample_dict[k] for k in sample_dict.keys()-keys}

print(result_dict)

