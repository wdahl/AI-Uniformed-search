foundG = False
def recursionDFS(graph, start, states = [], path = []): 
    global foundG   
    states.append(start)
    path.append(start)
    if start is 'G':
        foundG = True

    if foundG == True:
        return states, path

    for nextNode in graph[start]:
        if foundG == True:
            return states, path
            
        if nextNode not in states:
            states, path = recursionDFS(graph, nextNode, states, path)
            if foundG == False:
                path.pop()

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

states, path = recursionDFS(undirectedGraph, 'S')
print("States Expanded: ", states)
print("Path Returned: ", path)