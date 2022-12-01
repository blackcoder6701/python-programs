def addition(num):
    if num:
        result=num+addition(num-1)
        return result
    else:
        return 0 
    
res= addition(5)
print(res)       