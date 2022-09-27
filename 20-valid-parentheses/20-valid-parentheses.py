class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        graph = {"(":")","{":"}","[":"]"}
        for i in s:
            if i in graph or not stack:
                stack.append(i)
            elif stack[-1] in graph and graph[stack[-1]] == i :
                stack.pop()
            else :
                stack.append(i)
                
        return not stack
    