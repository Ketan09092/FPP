class fibo:
    def __init__(self,n):
        self.n = n
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
     