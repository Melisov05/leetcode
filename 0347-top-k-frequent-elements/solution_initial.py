import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_nums = [0] * 2005
        for i in range(len(nums)):
            if nums[i] < 0:
                value = abs(nums[i])
            if nums[i] >= 0:
                value = nums[i] + 1000
            freq_nums[value] = freq_nums[value] + 1

        heap = []
        for i, el in enumerate(freq_nums):
            if el == 0:
                continue


            heapq.heappush(heap, (el,i))
            if len(heap) > k:
                heapq.heappop(heap)

        final = []
        for value, index in heap:
            if(index > 1000):
                final.append(index - 1000)
            elif(index < 1000):
                final.append(index * (-1))
            else:
                final.append(0)

        return final