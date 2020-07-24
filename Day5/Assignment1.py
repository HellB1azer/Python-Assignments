lst1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
lst1.sort()
str(i)
for i in lst1:
  if i==0:
    lst1.remove(i)
    lst1.append(i)
print(lst1)