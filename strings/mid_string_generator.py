#  Create a string made of the middle three characters

inp= input("enter the string: ")

#calculating the length of the string 

x=len(inp)

#getting the mid values

if x%2 == 0:
    mid=int(x/2)
    print("ohh ! its an even length string ")
else:
    mid =int((x+1)/2)
    print(mid)

#calculating the first and last letters


lastletter=int(mid+1)    
first_letter=int(mid-1)

print(inp[first_letter]+inp[mid]+inp[lastletter])

    
#another way(best way)

res=inp[mid-1:mid+2]
print(res)


