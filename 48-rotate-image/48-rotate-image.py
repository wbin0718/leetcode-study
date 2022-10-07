class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        graph = []
        n = len(matrix)
        for r in range(n):
            for c in range(n):
                if (r,c) not in graph and (c,r) not in graph:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                    graph.append((r,c))
                    graph.append((c,r))
                    
        for c in range(n//2):
            for r in range(n):
                matrix[r][c], matrix[r][-1-c] = matrix[r][-1-c], matrix[r][c]
            
        