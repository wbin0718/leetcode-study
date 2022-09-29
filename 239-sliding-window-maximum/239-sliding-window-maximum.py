from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        graph = []
        queue = deque()
        for i,n in enumerate(nums):
            while queue and nums[queue[-1]] <= n:
                queue.pop()
            
            queue += [i]
            
            if i - queue[0] >= k:
                queue.popleft()
            if i + 1 >= k:
                graph.append(nums[queue[0]])
        
        return graph
            