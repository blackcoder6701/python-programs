# Remove all occurrences of a specific item from a list.

list1 = [5, 20, 15, 20, 25, 50, 20]
twenty=[]
for i in range(1,len(list1)):
    if list1[i] == 20:
        twenty.append(i)
        # list1.pop(i)
print(twenty)
print(list1)
for j in range(1,len(twenty)):
    list1.pop(twenty[j])
