from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]
        def BFS(x,y):
            queue = deque()
            queue.append((x,y))
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            cnt = 1
            visited[x][y] = 1
            while queue:
                x,y = queue.popleft()
                
                for i in range(len(dx)):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or ny < 0 or nx >= n or ny >= m :
                        continue
                    
                    if grid[nx][ny] == "1" and visited[nx][ny] == 0 :
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
                        cnt += 1
            
            if cnt >0 :
                return 1
            else :
                return 0
            
        cnt = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == "1" and visited[x][y] == 0:
                    
                    cnt += BFS(x,y)
                    
        
        return cnt
                
                
                
        
            
        
        