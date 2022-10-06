#Q11
# Simple Interest
import math
P = float(input("Enter Prinicipal amount"))
R = float(input("Enter rate of interst"))
t = float(input("Enter number of years"))
si = ((P*R*t)/100)
print("Simple interst is", si)
d = ( 1+(R/100))
l = math.pow(d,t)
A = P*l
ci = A + P
print("Compound interest is", ci)