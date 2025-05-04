import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.vertices.update([u, v])

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        visited = set()
        heap = [(0, start)]

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            for neighbor, weight in self.adj[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 5)
g.add_edge('B', 'D', 10)
g.add_edge('C', 'E', 3)
g.add_edge('E', 'D', 4)
g.add_edge('D', 'F', 11)

distances = g.dijkstra('A')
for vertex, distance in sorted(distances.items()):
    print(f"Distance from A to {vertex}: {distance}")
