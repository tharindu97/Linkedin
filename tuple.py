# List
# x = [1,2,3,4]
# Tuple
# y = (1,2,3,4)
# print(x)
# print(y[0])
# print(len(y))
# z = (1,3,4.5,'python')
#
# x = y+z
# print(x)

# x = ()
# y = ('java')
# z = ('python', 'java')


# x = (1,2,3,4)
# del x
# print(x)

import timeit
list_time = timeit.timeit(stmt="[1,2,3,4,5]")
tuple_time = timeit.timeit(stmt="(1,2,3,4,5)")
print(list_time*1000)
print(tuple_time*1000)
