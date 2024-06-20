import heapq

def dijkstra(graph, start):
    
    queue = []
    heapq.heappush(queue, (0, start))

    
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    
    path = {vertex: None for vertex in graph}

    while queue:
        
        current_distance, current_vertex = heapq.heappop(queue)

        
        if current_distance > distances[current_vertex]:
            continue

        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return distances, path


if __name__ == "__main__":
   
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_vertex = 'A'
    distances, paths = dijkstra(graph, start_vertex)

    print("Shortest distances from start vertex:")
    for vertex, distance in distances.items():
        print(f"Distance to {vertex}: {distance}")

    print("\nPaths from start vertex:")
    for vertex, prev in paths.items():
        print(f"Path to {vertex}: {prev}")
