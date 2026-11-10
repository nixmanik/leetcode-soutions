"""

0023. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

"""
# Imports for local running, not needed on leetcode
import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Priority Queue approach (using Python min-heap heapq)
        heap = []
        for head in lists:
            # if no head, it's an empty list
            if head:
                # using id() collects the memory address as a unique identifier that gets compared by heappop if the values are equal 
                heapq.heappush(heap, (head.val, id(head), head))
        # dummy node onto which the merged list is built
        dummy = ListNode()
        current = dummy
        # while loop will continue until nothing is left
        while heap:
            # Extract heappop'd node, the id isn't needed for anything after this
            val, _, node = heapq.heappop(heap)
            # node should now refer to the smallest val node in the lists (the lists are all ascending ordered)
            current.next = node
            current = current.next
            # push the next node on the list if there is one
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))
        # Merged list starts just after the dummy
        return dummy.next

"""

AI was used to understand how to get around sorting the tuples without it breaking when counting identical values. Initially I used a counter variable, but read about id() and how it takes the memory address and tried it out to remove the need for another variable. Seems to work fine

"""