class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(value,i) for i,value in enumerate(nums)]
        nums = sorted(nums, key=lambda x : x[0])
        left = 0
        right = len(nums) - 1
        
        while left < right :
            
            tmp = nums[left][0] + nums[right][0]
            if target == tmp:
                return [min(nums[left][1], nums[right][1]), max(nums[left][1],nums[right][1])]
            elif tmp > target:
                right -= 1
            elif tmp < target:
                left += 1