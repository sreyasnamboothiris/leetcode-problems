# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(current_node,prev):
            if current_node is None:
                return prev
            next_node = current_node.next
            current_node.next = prev
            return reverse(next_node,current_node)
        head = reverse(head,None)
        return head
        