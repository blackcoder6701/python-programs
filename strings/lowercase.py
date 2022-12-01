# Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"

#delcaring the two lists

lower=[]
upper=[]


for i in range(len(str1)):
    if str1[i].islower():
        lower.append(str1[i])
    else:
        upper.append(str1[i])

final_result=lower+upper


for i in final_result:
  print(i,end="")
