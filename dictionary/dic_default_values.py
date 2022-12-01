# Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}


# fromkeys ,functions takes the input and makes the dict

result_dict = dict.fromkeys(employees,defaults)
print(result_dict)


#printing both the dicts individally


print(result_dict['Kelly'])
print(result_dict['Emma'])