# write a program to find the euclidean distance btw two coordinates, take both the coordinates from the user as input.
x1 = float(input('enter value of x1: '))
x2 = float(input('enter vlaue of x2: '))
y1 = float(input('enter value of y1: '))
y2 = float(input("enter value of y2: "))
d = ((x2-x1)**2+(y2-y1)**2)**0.5
print('euclidean distance', d)