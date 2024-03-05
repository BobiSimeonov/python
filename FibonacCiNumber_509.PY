class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        elif n == 2:
            return 1
        dicty = {1:0, 2:1}
        
        def fibo(m):
            dicty[m] = dicty[m-1] + dicty[m-2]
            if m == n:
                return dicty[m]+dicty[m-1]
            return fibo(m+1)
        
        return fibo(3)




n = 0
solution = Solution()
print(solution.fib(n))