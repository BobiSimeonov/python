class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = - 1
        for i in range (0, len(haystack), 1):
            if len(needle) > len(haystack) - i:
                return -1
            for j in range(0, len(needle), 1):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i

        return result
    


haystack = "mississippi"
needle = "issipi"
solution = Solution()
print(solution.strStr(haystack, needle))
