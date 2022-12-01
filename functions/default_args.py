# Write a program to create a function show_employee() using the following conditions.

# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def showEmployee(name,salary=9000):
    print("name:{name} Salary : {salary}".format(name=name,salary=salary))



showEmployee("Ben", 12000)

#here as the salary is not specified the default arg will be taken
showEmployee("Jessa")