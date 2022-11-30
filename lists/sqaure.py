# Turn every item of a list into its square
list1=[2,3,4,5,6,7,8]
final_list=[]
for i in range(len(list1)):
    result = list1[i]*list1[i]
    final_list.append(result)
print(final_list)