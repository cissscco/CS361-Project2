import heapq
import time
import tracemalloc

from ArrayDijkstra import sparseA, sparseb, densea, denseb, dense3


def matrix_to_list(matrix):
    graph = {}

    for i in range(len(matrix)):
        graph[i] = []

        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                graph[i].append((j, matrix[i][j]))

    return graph


def dijkstra_heap(graph, source):
    distance = [float('inf')] * len(graph)
    distance[source] = 0

    heap = []
    heapq.heappush(heap, (0, source))

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > distance[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            if weight > 0 and current_dist + weight < distance[neighbor]:
                distance[neighbor] = current_dist + weight
                heapq.heappush(heap, (distance[neighbor], neighbor))

    return distance




def run_heap_once_for_report(graph, source):
    tracemalloc.start()
    start_time = time.perf_counter()

    distances = dijkstra_heap(graph, source)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return distances, end_time - start_time, peak


if __name__ == "__main__":
    print("Sparse Graph 1:")
    distances, runtime, memory = run_heap_once_for_report(sparseA, 0)
    for i in range(len(distances)):
        print(f"Node: {chr(ord('A') + i)}  Shortest Path: {distances[i]}")
    print(f"Time used: {runtime:.8f} seconds")
    print(f"Memory: {memory} B\n")

    print("Sparse Graph 2:")
    distances, runtime, memory = run_heap_once_for_report(sparseb, 0)
    for i in range(len(distances)):
        print(f"Node: {i + 1}  Shortest Path: {distances[i]}")
    print(f"Time used: {runtime:.8f} seconds")
    print(f"Memory: {memory} B\n")

    print("Dense Graph 1:")
    distances, runtime, memory = run_heap_once_for_report(matrix_to_list(densea), 0)
    for i in range(len(distances)):
        print(f"Node: {chr(ord('A') + i)}  Shortest Path: {distances[i]}")
    print(f"Time used: {runtime:.8f} seconds")
    print(f"Memory: {memory} B\n")

    print("Dense Graph 2:")
    distances, runtime, memory = run_heap_once_for_report(matrix_to_list(denseb), 0)
    for i in range(len(distances)):
        print(f"Node: {i + 1}  Shortest Path: {distances[i]}")
    print(f"Time used: {runtime:.8f} seconds")
    print(f"Memory: {memory} B\n")

    print("Dense Graph 3:")
    distances, runtime, memory = run_heap_once_for_report(matrix_to_list(dense3), 0)
    for i in range(len(distances)):
        print(f"Node: {i + 1}  Shortest Path: {distances[i]}")
    print(f"Time used: {runtime:.8f} seconds")
    print(f"Memory: {memory} B\n")
