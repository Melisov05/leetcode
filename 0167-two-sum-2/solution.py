from typing import List

numbers = [2,3,4]; target = 6

class Solution():
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(numbers)):
            difference = target - numbers[i]

            if difference in hash_map:
                return [hash_map[difference] +1, i + 1]
            else:
                hash_map[numbers[i]] = i

sol = Solution()
print(sol.twoSum(numbers, target))