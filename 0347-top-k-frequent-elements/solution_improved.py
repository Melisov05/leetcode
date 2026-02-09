import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        SHIFT = 1000
        freq_nums = [0] * 2001
        for i in nums:
            freq_nums[i + SHIFT] += 1

        heap = []
        for i, el in enumerate(freq_nums):
            if el == 0:
                continue
            heapq.heappush(heap, (el,i))
            if len(heap) > k:
                heapq.heappop(heap)

        return [idx - SHIFT for el, idx in heap]
