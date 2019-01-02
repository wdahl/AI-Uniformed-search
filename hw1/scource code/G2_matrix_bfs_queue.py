def bfs(matrix, start):
    states = []
    queue = [start]
    parents = {}
    while queue:
        currElement = queue.pop(0)
        if currElement not in states:
            states += [currElement]
            if currElement is 6:
                path = [currElement]
                while currElement is not 11:
                    path += [parents[currElement]]
                    currElement = parents[currElement]

                path.reverse()
                return states, path

            count = 0
            for nextElement in matrix[currElement]:
                if nextElement == 1:
                    if count not in states:
                        queue += [count]
                        if count not in parents:
                            parents[count] = currElement
                
                count += 1

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

states, path = bfs(matrix, 11)
letterStates = []
letterPath = []
maps = {0 : 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'P', 9: 'Q', 10: 'R', 11: 'S'}
for state in states:
    letterStates += maps[state]

for elements in path:
    letterPath += maps[elements]

print("States Expanded: ", letterStates)
print("Path Returned: ", letterPath)