# Write a program to create a function that takes two arguments, name and age, and print their value.

name=input("enter your name: ")
age=input("enter  your age: ")

def details(name,age):
    print("your age is {age}".format(age=age))
    print("your age is {name}".format(name=name))


#calling the fucntion

details(name, age)

