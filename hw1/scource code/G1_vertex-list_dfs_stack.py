def stackDFS(graph, start):
    stack = [start]
    states = []
    path = []
    while stack:
        newstack = []
        currNode = stack.pop()
        if currNode not in states:
            path += [currNode]
            states += [currNode]
            if currNode is 'G':
                return states, path

            count = 0    
            for nextNode in graph[currNode]:
                if nextNode not in states:
                    count += 1

                newstack += [nextNode]

            newstack.reverse()
            stack += newstack
            if count == 0:
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

states, path = stackDFS(undirectedGraph, 'S')
print("States Expanded: ", states)
print("Path Returned: ", path)