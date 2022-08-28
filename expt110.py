import fibonacci
n=int(input("enter the range:"))
if(n<0):
    print("enter the valid range:")
else:
    print("the range is:\n")
    fibonacci.fibonacci(n)
