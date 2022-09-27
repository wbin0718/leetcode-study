class Solution:
    def fib(self, n: int) -> int:
        graph = [0] * 31
        graph[0] = 0
        graph[1] = 1
        for i in range(2,n+1):
            graph[i] = graph[i-1] + graph[i-2]
        
        return graph[n]
        