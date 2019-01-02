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
    path = [start]
    unsorted_path = []
    neighbors = get_neighbors(graph, start)
    for neighbor in neighbors:
        weight = get_weight_of_edge(graph, start, neighbor)
        queue.insert_with_priority((neighbor, weight), weight)

    total_cost = -1
    while not queue.is_empty():
        curr_vertext, cost = queue.pull_highest_priority()
        if curr_vertext not in states:
            states += [curr_vertext]
            if curr_vertext is 6:
                while not queue.is_empty():
                    curr_vertext, new_cost = queue.pull_highest_priority()
                    if new_cost == cost:
                        if curr_vertext not in unsorted_path:
                            unsorted_path += [curr_vertext]

                count = 0
                while count < len(unsorted_path):
                    index = 0
                    for element in graph[start]:
                        if element is not 0:
                            if index in unsorted_path:
                                if index not in path:
                                    path += [index]
                                    break

                        index += 1
                            
                    start = index
                    count += 1

                if 6 not in path:
                    path += [6]
                    
                return states, path

        neighbors = get_neighbors(graph, curr_vertext)
        if neighbors:
            for neighbor in neighbors:
                total_cost = get_weight_of_edge(graph, curr_vertext, neighbor) + cost
                queue.insert_with_priority((neighbor, total_cost), total_cost)

    return states, path

matrix = [[0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [2, 0, 0, 8, 0, 3, 0, 0, 0, 0, 0, 0],
          [0, 1, 8, 0, 2, 0, 0, 0, 0, 0, 0, 3],
          [0, 0, 0, 2, 0, 0, 0, 8, 0, 0, 2, 9],
          [0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0],
          [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 8, 0, 0, 0, 4, 4, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 4, 0, 15, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 4, 15, 0, 0, 0],
          [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
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