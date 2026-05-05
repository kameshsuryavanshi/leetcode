# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge cases: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find length and the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Optimize k
        # If k is a multiple of length, rotation results in the same list
        k = k % length
        if k == 0:
            return head
        
        # Step 3: Find the new tail (which is at index length - k - 1)
        # The new head will be at index length - k
        steps_to_new_tail = length - k - 1
        current = head
        
        for _ in range(steps_to_new_tail):
            current = current.next
        
        # Step 4: Perform the rotation
        new_head = current.next
        current.next = None       # Break the list
        tail.next = head          # Connect old tail to old head
        
        return new_head