l = [22,33,44]
print(l)
n=int(input("Enter the value to Change:"))
m=int(input("Enter the value to Update:"))
i = l.index(n)
l = [m]+l[i:]
l.remove(n)
print(l)
