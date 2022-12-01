# Append new string in the middle of a given string

inp_str =input("enter the string : ")
add_str=input("enter the string to add in middle: ")

x=len(inp_str)
if x%2 == 0:
    mid=int(x/2)
    print("ohh ! its an even length string ")
else:
    mid =int((x+1)/2)
    print(mid)

print(inp_str[:mid]+add_str+inp_str[mid:])