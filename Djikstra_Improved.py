import heapq

def dijkstra(graph, start):
    # Check for negative weights in the graph
    for vertex, edges in graph.items():
        for neighbor, weight in edges.items():
            if weight < 0:
                raise ValueError("Graph contains a negative weight. Dijkstra's algorithm requires all weights to be non-negative.")

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
