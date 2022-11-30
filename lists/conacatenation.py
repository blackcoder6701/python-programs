list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
final_result=[]
if len(list1)==len(list2):
    for i in range(len(list1)):
        final_list=list1[i]+list2[i]
        final_result.append(final_list)
    print(final_result)
else:
    print("enter equal length list")
    