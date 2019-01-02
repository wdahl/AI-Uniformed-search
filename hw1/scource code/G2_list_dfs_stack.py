def dfs(graph, start):
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
                while path:
                    node = path.pop()
                    newCount = 0
                    for children in graph[node]:
                        if children not in states:
                            newCount = 1
                            break

                    if newCount == 1:
                        path += node
                        break

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

states, path = dfs(graph, 'S')
print("States Expanded: ", states)
print("Path Returned: ", path)