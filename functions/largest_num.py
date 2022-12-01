def largestnum(x):
    x.sort()
    return x[-1]



list_of_numbers = [4, 6, 8, 24, 12, 2]
largestnum(list_of_numbers)
largestnum( [4, 6, 8, 24, 12, 2])

#using the sorting method

list_of_numbers.sort()
print(list_of_numbers[-1])

#another method 

print(max(list_of_numbers))