# write a program to find the simple interest when the value of principle, rate of interest and time period is provided by the user
P = float(input('enter vlaue of principle interest:'))
R = float(input('enter vlaue of rate of interest:'))
T = float(input('enter value of time period:'))
SI = P*R*T/100
print("simple intrest", SI)