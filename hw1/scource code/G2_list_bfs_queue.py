def bfs(graph, start):
    states = []
    queue = [start]
    parents = {}
    while queue:
        currNode = queue.pop(0)
        if currNode not in states:
            states += [currNode]
            if currNode is 'G':
                path = [currNode]
                while currNode is not 'S':
                    path += parents[currNode]
                    currNode = parents[currNode]

                path.reverse()
                return states, path

            for nextNode in graph[currNode]:
                queue += [nextNode]
                if nextNode not in parents:
                    parents[nextNode] = currNode

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