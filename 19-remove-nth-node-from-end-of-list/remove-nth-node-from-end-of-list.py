# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        
        fast_pointer = dummy_node
        slow_pointer = dummy_node
        
        for _ in range(n):
            fast_pointer = fast_pointer.next
        
        while fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        
        slow_pointer.next = slow_pointer.next.next
        
        return dummy_node.next