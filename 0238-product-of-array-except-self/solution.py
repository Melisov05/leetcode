from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]*nums[i-1])

        suffix = [1]
        for i in range(-2, -len(nums)-1, -1):
            suffix.append(suffix[-1]*nums[i+1])

        suffix.reverse()

        final = []
        for i in range(len(nums)):
            final.append(suffix[i] * prefix[i])

        return final


