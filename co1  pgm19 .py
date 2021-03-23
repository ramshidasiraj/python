dict1 = {}
dict2 = {}
dict3 = {}
n1 = int(input("enter total number of elements in the dict1 : "))
for i in range(n1):
    dict1[i] = int(input("enter the elements : "))
print(dict1)
n2 = int(input("enter the total number of elements in the dict2 : "))
for i in range(n2):
    dict2[i] = int(input("enter the elements : "))
print(dict2)
for i in dict1:
    if i not in dict2:
        new = {i : dict1[i]}
        dict3.update(new)
    else:
        new = {i : dict1[i]+dict2[i]}
        dict3.update(new)
for i in dict2:
    if i not in dict2:
        new = {i : dict2[i]}
        dict3.update(new)
print(dict3)


