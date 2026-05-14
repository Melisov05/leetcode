from typing import List

nums = [0,3,7,2,5,8,4,6,0,1]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best_count = 0
        hash_set = set(nums)

        
        for num in hash_set:
            if num -1 not in hash_set:
                start = num
                current_counter = 1
                j = 1
                while start + j in hash_set:
                    current_counter+=1
                    j+=1
                
                if current_counter > best_count:
                    best_count = current_counter
            
    
        return best_count
    

sol = Solution()

print(sol.longestConsecutive(nums))


        