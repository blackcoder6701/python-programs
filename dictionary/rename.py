sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}


x=sample_dict.keys()
print(x)



if 'city' in x:
    sample_dict['location']= sample_dict.pop('city')

print(sample_dict)