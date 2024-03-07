class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and i == len(s) - 1 or s[i] == " " and s[i+1] == " ":
                continue
            if s[i] == " ":
                break
            counter +=1
        return counter
    
s = "   fly me   to   the moon  "
solution = Solution()
print(solution.lengthOfLastWord(s))