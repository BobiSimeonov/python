class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        for i in range (0, 32, 1):
            if 3**i == n:
                return True 
            
        return False


n = 27
solution = Solution()
print(solution.isPowerOfThree(n))