from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        string1 = ""
        string2 = ""

        while True:
            string1 += str(l1.val)
            if l1.next != None:
                l1 = l1.next
            else:
                break
            
        firstNum = int(string1[::-1])

        while True:
            string2 += str(l2.val)
            if l2.next != None:
                l2 = l2.next
            else:
                break
        secondNum = int(string2[::-1])

        sum = str(firstNum + secondNum)
        for x in range (0, len(sum), 1):
            if x == 0:
                result = ListNode(int(sum[x]), None)
            else:
                result = ListNode(int(sum[x]), result)

        return result
        

        
v3 = ListNode(3)
v2 = ListNode(4,v3)
v1 = ListNode(2, v2)

z3 = ListNode(4)
z2 = ListNode(6, z3)
z1 = ListNode(5, z2)

solution = Solution()
result = solution.addTwoNumbers(v1, z1)
print(result.val)