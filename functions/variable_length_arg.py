# Write a program to create function func1() to accept a variable length of arguments and print their value.

def varible_args(*args):
    x=args
    print(x)
    for i in x:
        print(i)
    
varible_args(10,35,67)

varible_args(14,34,5,6)


