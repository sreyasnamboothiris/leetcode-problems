# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_gcd(self,a,b):
            while b:
                a, b = b, a%b
            return a
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        if current_node.next is None:
            return head
        while current_node.next:
            gcd_val = self.find_gcd(current_node.val,current_node.next.val)
            gcd_node = ListNode(gcd_val)
            gcd_node.next = current_node.next
            current_node.next = gcd_node
            current_node = gcd_node.next
        return head
        

        
        