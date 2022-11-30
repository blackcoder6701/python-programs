#  Iterate both lists simultaneously
list1=[10,47,56,8,9]
list2=[34,56,8,9,90]
print(list2[::-1])
# zip()=> it taken two or more tuples,lists,etc as args and can be displayed as single unit
for x,y in zip(list1,list2[::-1]):
    print(x,y)
    
