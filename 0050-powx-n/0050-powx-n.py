class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            is_negative = True
            n = abs(n)
        else:
            is_negative = False
        
        def solve(x,n):
            if n == 0:
                return 1
            half = solve(x,n//2)
            if n%2 == 0:
                return half*half
            else:
                return half*half*x

        ans = solve(x,n)

        if is_negative:
            return 1/ans
        return ans


        