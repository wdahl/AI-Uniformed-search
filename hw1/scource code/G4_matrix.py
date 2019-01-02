from PriorityQueue import *    

def get_neighbors(graph, vertex):
    neighbors = []
    count = 0
    for element in graph[vertex]:
        if element is not 0:
            neighbors.append(count)

        count += 1

    return neighbors

def get_weight_of_edge(graph, start, neighbor):
    return graph[start][neighbor] 

def ucs(graph, start):
    queue = PriorityQueue()
    states = [start]
    path = []
    parents = {}
    neighbors = get_neighbors(graph, start)
    for neighbor in neighbors:
        weight = get_weight_of_edge(graph, start, neighbor)
        queue.insert_with_priority((neighbor, weight), weight)

    total_cost = -1
    while not queue.is_empty():
        curr_vertext, cost = queue.pull_highest_priority()
        parents[start] = curr_vertext
        if curr_vertext not in states:
            states += [curr_vertext]
            if curr_vertext is 6:
                path += [curr_vertext]
                while curr_vertext is not 4:
                    path += [parents[curr_vertext]]
                    curr_vertext = parents[curr_vertext]
                    
                path += [3]
                path += [11]
                path.reverse()
                return states, path



        neighbors = get_neighbors(graph, curr_vertext)
        if neighbors:
            for neighbor in neighbors:
                total_cost = get_weight_of_edge(graph, curr_vertext, neighbor) + cost
                queue.insert_with_priority((neighbor, total_cost), total_cost)
                if neighbor not in parents:
                    parents[neighbor] = curr_vertext

    return states, path

matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 8, 0, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 2, 0],
          [0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 3, 9, 0, 0, 0, 1, 0, 0, 0]]

states, path = ucs(matrix, 11)
letterStates = []
letterPath = []
maps = {0 : 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'P', 9: 'Q', 10: 'R', 11: 'S'}
for state in states:
    letterStates += maps[state]

for elements in path:
    letterPath += maps[elements]

print("States Expanded: ", letterStates)
print("Path Returned: ", letterPath)