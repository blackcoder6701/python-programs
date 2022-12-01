# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

def calculation(a,b):
    sum1=a+b
    sub=a-b
    print("the sum of {a} and {b} is: {sum1}".format(a=a,b=b,sum1=sum1))
    print("the subtraction of {a} and {b} is: {sub}".format(a=a,b=b,sub=sub))
    
result=calculation(2, 3)
