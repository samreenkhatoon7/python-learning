# write a programe that will tell the number of dogs and chicken are there where the user will provide the value of total head and leg
h = float(input('enter number of head: '))
l = float(input('enter number of leg:',))
c = (4*h-l)/2
# c= chicken
d = h-c
print('no. of chicken', c)
print('no. of dog',d)