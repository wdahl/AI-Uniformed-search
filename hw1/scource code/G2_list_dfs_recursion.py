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

states, path = recursionDFS(graph, 'S')
print("States Expanded: ", states)
print("Path Returned: ", path)