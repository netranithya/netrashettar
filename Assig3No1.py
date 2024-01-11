#Even number and odd number

checklist=[10,501,22,37,100,999,87,351]
evenlist=[]
oddlist=[]
for x in checklist:
    if x%2==0:
       evenlist.append(x)
    else:
        oddlist.append(x)
print("even no=", evenlist)
print("odd no=", oddlist)