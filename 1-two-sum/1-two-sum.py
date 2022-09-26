class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        graph = {value:key for key,value in enumerate(nums)}
        for i,value in enumerate(nums):
            if (target - value) in graph and i != graph[(target-value)]:
                return [i, graph[(target-value)]]
        