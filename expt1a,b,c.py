x=10
y=20
z=30
print("before swapping")
print("values of x and y and z",x,y,z)
temp=x
x=y
y=z
z=temp
print("after swapping")
print("values of x and y and z",x,y,z)


import cmath
a=10
b=20
c=30
d=(b**2)-(4*a*c)
ans1=(-b-cmath.sqrt(d))/(2*a)
ans2=(-b+cmath.sqrt(d))/(2*a)
print("the solution is",ans1,ans2)

a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
sum=a+b
print("the sum is",sum)
sub=a-b
print("the sub is",sub)
mul=a*b
print("the mul is",mul)
div=a/b
print("the div is",div)
