# given the 1st two term of an arithmetic series. find the nth term of the series assume all input are provided by the user
a = int(input('enter fisrt term: '))
b = int(input('enter second term: '))
n = int(input('enter n no. of term: '))
d = b-a # d= difference
An = (a +(n-1)*d)
print('nth term', An)