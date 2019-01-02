from PriorityQueue import *    

def get_neighbors(graph, vertex):
    neighbors = []
    for neighbor in graph[vertex]:
        neighbors += neighbor

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
            states += curr_vertext
            if curr_vertext is 'G':
                while not queue.is_empty():
                    curr_vertext, new_cost = queue.pull_highest_priority()
                    if new_cost == cost:
                        if curr_vertext not in unsorted_path:
                            unsorted_path += curr_vertext

                count = 0
                while count < len(unsorted_path):
                    for neighbor in graph[start]:
                        if neighbor in unsorted_path:
                            if neighbor not in path:
                                path += neighbor
                                break
                            
                    start = neighbor
                    count += 1

                if 'G' not in path:
                    path += 'G'

                return states, path

        neighbors = get_neighbors(graph, curr_vertext)
        if neighbors:
            for neighbor in neighbors:
                total_cost = get_weight_of_edge(graph, curr_vertext, neighbor) + cost
                queue.insert_with_priority((neighbor, total_cost), total_cost)

    return states, path

graph = {'S': {'D': 3, 'E': 9, 'P': 1},
         'D': {'B': 1, 'C': 8, 'E': 2, 'S': 3},
         'E': {'D': 2, 'H': 8, 'R': 2, 'S': 9},
         'P': {'H': 4, 'Q': 15, 'S': 1},
         'B': {'A': 2, 'D': 1},
         'C': {'A': 2,'D': 8, 'F': 3},
         'H': {'E': 8, 'P': 4, 'Q': 4},
         'R': {'E': 2, 'F': 2},
         'Q': {'H': 4, 'P': 15},
         'A': {'B': 2, 'C': 2},
         'F': {'C': 3, 'G': 2, 'R': 2},
         'G': {'F': 2}
         }

states, path = ucs(graph, 'S')
print("States Expanded: ", states)
print("Path Returned: ", path)