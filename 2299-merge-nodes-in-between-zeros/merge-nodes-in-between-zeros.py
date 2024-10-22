# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to simplify handling of head
        current = dummy  # Pointer to build the new list
        current_node = head.next  # Skip the initial '0' node
        val = 0
        
        while current_node:
            if current_node.val == 0:
                # Once we hit a 0, we add the sum as a new node
                current.next = ListNode(val)
                current = current.next  # Move current to this new node
                val = 0  # Reset sum
            else:
                val += current_node.val  # Add non-zero values
            current_node = current_node.next
        
        return dummy.next  # Return the head of the newly formed list

# Helper function to convert ListNode to a Python list (for testing or serialization)
def listnode_to_list(node: Optional[ListNode]) -> list:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
