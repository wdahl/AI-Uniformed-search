foundG = False
parents = {}
def bfs(graph, start = ['S'], states=[], path=[]):
    global foundG
    global parents
    nextLevel = []
    if len(start) > 0:
        for node in start:
            if foundG == True:
                return states, path

            if node not in states:
                states += [node]
                if node is 'G':
                    foundG = True
                    path = [node]
                    while node is not 'S':
                        path += parents[node]
                        node = parents[node]
                        
                    path.reverse()    
                    return states, path

            for nextNode in graph[node]:
                if nextNode not in states:
                    nextLevel += nextNode
                
                if nextNode not in parents:
                    parents[nextNode] = node

        states, path = bfs(graph, nextLevel, states, path)
            
    return states, path

graph = {'S': ['D', 'E', 'P'],
         'A': [],
         'C': ['A'],
         'D': ['B', 'C', 'E'],
         'B': ['A'],
         'G': [],
         'E': ['H', 'R'],
         'F': ['C', 'G'],
         'H': ['P', 'Q'],
         'P': ['Q'],
         'Q': [],
         'R': ['F']
         }

states, path = bfs(graph, 'S')
print("States Expanded: ", states)
print("Path Returned: ", path)