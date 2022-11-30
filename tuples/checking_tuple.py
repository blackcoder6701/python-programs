#  Check if all items in the tuple are the same
# enter the length of the tuple

def number_check(any_tuple):
    return all(i==any_tuple[0] for i in any_tuple)

tuple1=(45,45,34,45)

print(number_check(tuple1))
