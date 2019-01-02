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
            states += curr_vertext
            if curr_vertext is 'G':
                path += curr_vertext
                while curr_vertext is not 'D':
                     path += parents[curr_vertext]
                     curr_vertext = parents[curr_vertext]
                    
                path += 'S'
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

graph = {'S': {'D': 3, 'E': 9, 'P': 1},
         'D': {'B': 1, 'C': 8, 'E': 2},
         'E': {'H': 8, 'R': 2},
         'P': {'Q': 15},
         'B': {'A': 2},
         'C': {'A': 2},
         'H': {'P': 4, 'Q': 4},
         'R': {'F': 2},
         'Q': {},
         'A': {},
         'F': {'C': 3, 'G': 2},
         'G': {}
         }

states, path = ucs(graph, 'S')
print("States Expanded: ", states)
print("Path Returned: ", path)