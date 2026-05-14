from typing import List

numbers = [2,3,4]; target = 6

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            total_value = numbers[i] + numbers[j]
                
            if total_value == target:
                return [i+1, j+1]
            elif total_value > target:
                j-=1
            elif total_value < target:
                i+=1


sol = Solution()
print(sol.twoSum(numbers, target))
            
