def dfs(matrix, start):
    stack = [start]
    states = []
    path = []
    while stack:
        newstack = []
        currElement = stack.pop()
        if currElement not in states:
            path += [currElement]
            states += [currElement]
            if currElement == 6:
                return states, path

            children = 0
            count = 0    
            for nextElement in matrix[currElement]:
                if nextElement == 1:
                    if count not in states:
                        children += 1
                        newstack += [count]

                count += 1
                if count == 11:
                    break

            newstack.reverse()
            stack += newstack

            if children == 0:
                path.pop()
                while path:
                    added = False
                    node = path.pop()
                    newCount = 0
                    for child in matrix[node]:
                        if child == 1:
                            if newCount not in states:
                                path += [node]
                                added = True
                                break
                    
                        newCount += 1
                        
                    if added == True:
                        break

    return states, path

matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
          [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]]

states, path = dfs(matrix, 11)
letterStates = []
letterPath = []
maps = {0 : 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'P', 9: 'Q', 10: 'R', 11: 'S'}
for state in states:
    letterStates += maps[state]

for elements in path:
    letterPath += maps[elements]

print("States Expanded: ", letterStates)
print("Path Returned: ", letterPath)