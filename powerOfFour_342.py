class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 4 != 0:
            return False
        for i in range (0, 32, 1):
            if 4**i == n:
                return True 
            
        return False


n = 1
solution = Solution()
print(solution.isPowerOfFour(n))