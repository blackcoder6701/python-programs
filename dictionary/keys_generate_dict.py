#  Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
    }


# Keys to extract
keys = ["name", "salary"]
new_dict={k: sample_dict[k] for k in keys}
print(new_dict)


# x,y=sample_dict['name'],sample_dict['salary']

# print(x)
# print(y)



# result_dict={"name":x,"salary":y}
# print(result_dict)