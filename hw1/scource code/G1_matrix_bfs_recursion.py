foundG = False
parents = {}
def bfs(matrix, start, states=[], path=[]):
    global foundG
    global parents
    nextLevel = []
    if len(start) > 0:
        for elements in start:
            if foundG == True:
                return states, path

            if elements not in states:
                states += [elements]
                if elements is 6:
                    foundG = True
                    path = [elements]
                    while elements is not 11:
                        path += [parents[elements]]
                        elements = parents[elements]
                        
                    path.reverse()    
                    return states, path

            count = 0
            for nextElement in matrix[elements]:
                if nextElement == 1:
                    if count not in states:
                        nextLevel += [count]
                
                        if count not in parents:
                            parents[count] = elements

                count += 1

        states, path = bfs(matrix, nextLevel, states, path)
            
    return states, path

matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
         [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]]

start = list()
start.append(11)
states, path = bfs(matrix, start)
letterStates = []
letterPath = []
maps = {0 : 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'P', 9: 'Q', 10: 'R', 11: 'S'}
for state in states:
    letterStates += maps[state]

for elements in path:
    letterPath += maps[elements]

print("States Expanded: ", letterStates)
print("Path Returned: ", letterPath)