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
         'R': ['E', 'F']
         }

states, path = bfs(undirectedGraph, 'S')
print("States Expanded: ", states)
print("Path Returned: ", path)