inp_string_first=input("enter the first string:")
inp_string_second=input("enter the second string: ")

def concat(inp_string1,inp_string2):
    first=inp_string1[0]+inp_string2[0]
    
    x=len(inp_string1)
    y=len(inp_string2)
    
    #getting the mid values
    
    if x%2 == 0:
        
        mid=int(x/2)
    
    
    else:
        mid =int((x+1)/2)
    
    if y%2 == 0:
        
        mid1=int(y/2)
        
    
    else:
        mid1 =int((y+1)/2)
        
    mid_final=inp_string1[mid]+inp_string2[mid1]
    print(mid_final)
    
    last=inp_string1[-1]+inp_string2[-1]
    print(last)
    
    return first+mid_final+last  

concat(inp_string_first,inp_string_second)     

    