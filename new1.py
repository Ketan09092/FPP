from collections.abc import Iterable


class fibo:
    def __init__(self,n):
        self.n = n
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __dir__(self) -> Iterable[str]:
        pass
    def __str__(self) -> str:
        pass