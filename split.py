# def cstolot(str):
#     lot = []
#     for i in str.split(";"):
#         lot.append(tuple(i.split("=")))
#     return lot

# cs="a=b;c=d;e=f;g=h"
# a=cstolot(cs)
# print(a)
# print(type(a))
# print(a[0][1])

"""def cstolot(cs):
    return [tuple(i.split("=")) for i in cs.split(";")]

cst="a=b;c=d;e=f;g=h"
a=cstolot(cst)
print(a)
print(type(a))
print(a[0][1])"""

def lottocs(lot):
    cs = ""
    for i in lot:
            cs += "=".join(i)+";"
            return cs.strip(";")
    
def lottocs1(lot):
      return ";".join(["=".join(i)for i in lot])