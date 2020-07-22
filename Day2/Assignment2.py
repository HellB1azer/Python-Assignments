no1=int(input("Enter any number "))
cnt=0
for i in list(range(1,no1+1)):
  if (no1%i)==0:
    cnt=cnt+1
if cnt==2:
  print(no1, " is a Prime number")
else:
  print(no1, " is not a Prime number")  