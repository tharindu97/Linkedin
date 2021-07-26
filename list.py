x = [2,3,4,5,5,6]
y = ['d','d', 'f', 'd']
z = [8, 'd', True, 'Tharindu', [2,4,5]]
x[0] = 0
# Add List
x.insert(2,'12')
print(x);
x.append(888)
print(x);

# Remove item for List
x.remove(5)
print(x)
x.pop()
print(x)

# Delete List
# del x
# print(x)

# Clear item for list
print(x)
x.clear()
print(x)

# How to Sort list
n = [3,8,1,8,4]
n.sort()
n.sort(reverse=True)
print(n)


a,b,c,d = [1,2,3,4]
print(a)
print(b)
print(c)
print(d)

e,r,*t = [1,2,3,4,5,6,7,8]
print(e)
print(r)
print(t)