class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        if list1.val >= list2.val:
            next_node = list2
            list2 = list2.next
        else:
            next_node = list1
            list1 = list1.next
        starting_node = next_node

        while True:
            if list1 == None:
                    next_node.next = list2
                    break
            if list2 == None:
                    next_node.next = list1
                    break

            if list1.val <= list2.val:
                next_node.next = list1
                next_node = next_node.next
                list1 = list1.next
            else:
                next_node.next = list2
                next_node = next_node.next
                list2 = list2.next
                
        return starting_node


l3=ListNode(4)
l2=ListNode(2,l3)
l1=ListNode(2)
r3=ListNode(4)
r2=ListNode(3, r3)
r1=ListNode(1)
solution = Solution()
result = solution.mergeTwoLists(l1, r1)


while True:
    print(result.val)
    result = result.next
    if result == None:
        break

