class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        result = 0
        dicty = {}
        for i in range(0, len(s)-1, 1):
            substring = [s[i]]
            temp = 1
            for j in range (i+1, len(s), 1):
                if s[j] in substring:
                    dicty[i] = temp
                    break
                else:
                    substring.append(s[j])
                    temp += 1
                    if j == len(s) - 1:
                        dicty[i] = temp

        for v in dicty.values():
            if v > result:
                result = v
        return result


s = "dvdf"
solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print(result)