class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index, item in enumerate(nums):
            diff=target-item
            if diff in seen:
                return [seen[diff], index]
            seen[item]=index