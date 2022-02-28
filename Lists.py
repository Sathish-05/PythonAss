l = [22,33,44]
#Adding Items
l[1]=66
print(l)
l.insert(2, "Sathish")
print(l)
l.append(77)
print(l)
m=[1,2]
l.extend(m)
print(l)
#Removing Items
l.remove(22)
print(l)
l.pop(1)
print(l)
#list slicing
print(l[1:3])
print(l[:3])
print(l[1:])
print(l[-1])
#list sorted
l.sort()
print(l)
l.reverse()
print(l)

