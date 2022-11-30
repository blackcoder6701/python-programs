# Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# for i in range(len(list1)):
#     if list[i]== None:
#         list1.pop(i)
#     # else:
#     #     list1.append()    
# print(list1)
result=list(filter(None,list1))
print(result)
