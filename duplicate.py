# Write a program to Remove Duplicates from a List.

def remove(list):
    unique=[]
    for item in list:
        if item not in unique:
            unique.append(item)
    return unique

l=[1,2,3,4,1,2]
nl=remove(l)
print(nl)