import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Use a dummy head to simplify building the new list
        dummy = ListNode(0)
        current = dummy
        heap = []
        
        # 1. Put the head of each list into the min-heap
        for i in range(len(lists)):
            if lists[i]:
                # We store (value, index) to handle cases where values are identical
                # This prevents the heap from trying to compare ListNode objects directly
                heapq.heappush(heap, (lists[i].val, i))
        
        # 2. Extract the minimum and move to the next node in that specific list
        while heap:
            val, i = heapq.heappop(heap)
            
            # Attach the smallest node found to our result list
            current.next = lists[i]
            current = current.next
            
            # Move the pointer of the used list forward
            lists[i] = lists[i].next
            
            # If there's a next node in that list, push it into the heap
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                
        return dummy.next