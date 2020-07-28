lst1 = [(1,2,3), [1,2], ['a','hit','less']]
lst2 = []
for each in lst1:
  #print(each)
  if type(each)==tuple:
    for y in each:
      lst2.append(y)
  elif type(each)==list:
    for x in each:
      lst2.append(x)
print(lst2) 