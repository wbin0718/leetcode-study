import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        
        for time in times:
            graph[time[0]].append((time[1],time[2]))
        INF = 1e9
        distance = [INF] * (n+1)
        def dijkstra(start):
            q = []
            heapq.heappush(q,(0,start))
            distance[start] = 0
            tmp = {}
            
            while q :
                
                dist, now = heapq.heappop(q)
                if now not in tmp :
                    tmp[now] = dist
                if distance[now] < dist :
                    continue
                for i in graph[now]:
                    cost = dist + i[1]
                    if cost < distance[i[0]]:
                        distance[i[0]] = cost
                        heapq.heappush(q,(cost,i[0]))
            return tmp
        
        cnt = dijkstra(k)
        if len(cnt) == n :
            return max(cnt.values())
        else :
            return -1    
            
                
        
        
        