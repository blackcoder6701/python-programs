# Create an inner function to calculate the addition in the following way

def parameter(a,b):
    def addition(a,b):
        return a+b
    add=addition(a, b)      
    
    print("the addition of two number is : ",add )
    
    print("the final ans after adding 5 :", add+5)


parameter(5,6)