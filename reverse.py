l=[1,2,3,5,4]

def sort_desc(list):
    sorted_list=sorted(list,reverse=True)
    return sorted_list

def sort_asc(list):
    sort_list=sorted(list)
    return sort_list

def reverse_list(list):
    rev_list=list[::-1]
    return rev_list

a=sort_desc(l)
print(a)

a=sort_asc(l)
print(a)

a=reverse_list(l)
print(a)