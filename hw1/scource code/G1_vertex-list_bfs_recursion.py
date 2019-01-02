foundG = False
parents = {}
def recursiveBFS(graph, start = ['S'], states=[], path=[]):
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

        states, path = recursiveBFS(graph, nextLevel, states, path)
            
    return states, path


undirectedGraph = {'S': ['D', 'E', 'P'],
         'A': ['B', 'C'],
         'C': ['A', 'D', 'F'],
         'D': ['B', 'C', 'E', 'S'],
         'B': ['A', 'D'],
         'G': ['F'],
         'E': ['D', 'H', 'R', 'S'],
         'F': ['C', 'G', 'R'],
         'H': ['E', 'P', 'Q'],
         'P': ['H', 'Q', 'S'],
         'Q': ['H', 'P'],
         'R': ['E', 'F'],
         }

states, path = recursiveBFS(undirectedGraph)
print("States Expanded: ", states)
print("Path Returned: ", path)