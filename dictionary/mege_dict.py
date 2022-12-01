dict_number_1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict_number_2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict_number_1.update(dict_number_2)
print(dict_number_1)


#another method defining the merge to merge the dict ("|")

def Merge(dict_number_1,dict_number_2):
    result= dict_number_1 | dict_number_2
    print(result)
    

Merge(dict_number_1, dict_number_2)