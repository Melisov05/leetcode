from typing import List


#Input: [[1,1],[-1,1]]
#Output: true

# Input: [[1,1],[-1,-1]]
# Output: false

# (2c - x, y)

class Solution:
    def lineReflection(self, coord: List[List[int]]) -> bool:
        points = set([(x, y) for x, y in coord])
        min_x = min(x for x, y in points)
        max_x = max(x for x, y in points)

        sum_x = min_x + max_x
        for x, y in points:
            if (sum_x - x, y) not in points:
                return False
        return True

# def main():
#     sol = Solution()
#     print(sol.lineReflection([[1,1],[-1,-1]]))
#
# main()
