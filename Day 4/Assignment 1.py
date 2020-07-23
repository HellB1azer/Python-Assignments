import re
str1="what we think we become. we are python programmers"
a=input("Enter substring  you want to find:- ")
match = re.finditer(a, str1)
pos = [mtch.start() for mtch in match]
print(pos)