a=10
def f():
    a=20
    def g():
        print(a)
    return g
