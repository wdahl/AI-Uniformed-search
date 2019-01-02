import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.index = 0

    def is_empty(self):
        return len(self.heap) == 0
    
    def insert_with_priority(self, edge, weight):
        heapq.heappush(self.heap, (weight, self.index, edge))
        self.index += 1

    def pull_highest_priority(self):
        return heapq.heappop(self.heap)[-1]
