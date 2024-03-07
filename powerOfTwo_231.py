# class Solution:    # First option
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n == 1:
#             return True
#         if n % 2 != 0:
#             return False
#         while True and n != 2:
#             n /= 2
#             if n % 2 != 0:
#                 return False 
            
#         return True
    

# class Solution:       # Second option
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n == 1:
#             return True
#         if n % 2 != 0:
#             return False
#         for i in range (0, 32, 1):
#             if 2**i == n:
#                 return True 
            
#         return False


class Solution:       # Third option
    def isPowerOfTwo(self, n: int) -> bool:
        if n / 2 == 1 or n == 1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n//2)
            

    
n = 1
solution = Solution()
print(solution.isPowerOfTwo(n))