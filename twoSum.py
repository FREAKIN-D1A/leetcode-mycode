"""
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        while i < len(nums):
            num = nums[i]
            complement = target - num
            if complement in seen:
                return [i, seen[complement]]
            seen[num] = i
            i += 1

"""

def twoSum( nums, target):
    seen = {}
    i = 0
    while i < len(nums):
        num = nums[i]
        complement = target - num
        if complement in seen:
            return [i, seen[complement]]
        seen[num] = i
        i += 1


ans = twoSum(  nums = [3,3], target = 6)
print(ans)