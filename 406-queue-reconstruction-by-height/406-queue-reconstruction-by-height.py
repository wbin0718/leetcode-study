class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people = sorted(people, key=lambda x : (-x[0],x[1]))
        graph = []
        for person in people :
            graph.insert(person[1],person)
            
        return graph
        