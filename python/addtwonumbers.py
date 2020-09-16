# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = map(str, [l1.val, l1.next.val, l1.next.next.val])
        y = map(str, [l2.val, l2.next.val, l2.next.next.val])
        
        x.reverse()
        y.reverse()
        
        print("".join(x))
