class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        l = self.fib(n-1)
        s = self.fib(n-2)
        return l+s

        