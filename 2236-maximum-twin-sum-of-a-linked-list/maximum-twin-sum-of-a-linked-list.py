# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        second_half = None
        while slow:
            next_node = slow.next
            slow.next = second_half
            second_half = slow
            slow = next_node
        
        # Step 3: Compute the maximum twin sum
        max_sum = 0
        first_half = head
        second_half_start = second_half
        
        while second_half_start:
            current_sum = first_half.val + second_half_start.val
            if current_sum > max_sum:
                max_sum = current_sum
            first_half = first_half.next
            second_half_start = second_half_start.next
        
        return max_sum