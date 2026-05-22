# take input from user and store date
fnum = input('enter first number:')
snum = input('enter second number:')
# add two variable
result = fnum + snum
# print result
print(result)
''' if we put first and second number 55 , 66 respectively
so our output will be 5566 not added the number bcz the input 
function in string form , to perform numberical addition we use
explicit type conversion such as int()to specify that the input
taken as integer'''
fnum = int(input("enter first number:"))
snum = int(input("enter sencond number:"))
result = fnum + snum
print(result)
''' or we can also declear interger in result = int(fnum)+int(snum) without  converting input into interger
int(input()) '''
# this code for basic python
