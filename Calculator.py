Addition=1 
Subtraction=2
print("Select Any One")
print("1.Addition")
print("2.Subtraction")
n=int(input())
if n>0 and n<2:
    a=int(input("Enter Number1:"))
    b=int(input("Enter Number2:"))
    if n==1:
        print("Addition:",a+b)
    else:
        print("Subtraction:",a-b)
else:
    print("Invalid Option")
