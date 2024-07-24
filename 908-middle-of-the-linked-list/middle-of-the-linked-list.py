# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = head
        f = head
        while m is not None and m.next is not None:
            f = f.next
            m = m.next.next
        return f

        