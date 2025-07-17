import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)  # Push number into heap
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Keep size of heap = k

        return min_heap[0]  # The kth largest element

