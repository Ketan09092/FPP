# l=[1,2,3,4]
# a=l[len(l)-1]
# l[len(l)-1]=l[0]
# l[0]=a
# print(l)

def swap(ls):
    ls[0],ls[-1]=ls[-1],ls[0]
    return ls

ls=[1,2,3,4]
print("Old list :",ls)
nls=swap(ls)
print("New list:",nls)
