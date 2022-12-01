# Remove items from the set at once

set_of_numbers = {10, 20, 30, 40, 50}
remove_set={10,20,30}



# final_set= set_of_numbers-remove_set
# print(final_set)


set_of_numbers.difference_update({10,20,30})
print(set_of_numbers)


# for i in range(len(set_of_numbers)):
#     if set_of_numbers[i]>30:
#         final_set=set_of_numbers.remove(i)
#     print(final_set)


