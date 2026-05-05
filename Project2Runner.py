import time
import tracemalloc
import contextlib
import io

with contextlib.redirect_stdout(io.StringIO()):
    import ArrayDijkstra
    import MinHeap


TRIALS = 5


def count_edges(graph, is_matrix):
    # So the report table can show the number of edges
    if is_matrix:
        edges = 0

        for i in range(len(graph)):
            for j in range(i + 1, len(graph[i])):
                if graph[i][j] != 0:
                    edges += 1

        return edges

    total = 0

    for vertex in graph:
        total += len(graph[vertex])

    return total // 2


def run_array_average(graph, source, is_matrix):
    # Averaging the array version over 5 runs
    total_time = 0
    total_memory = 0
    final_distances = None

    for _ in range(TRIALS):
        tracemalloc.start()
        start_time = time.perf_counter()

        final_distances = ArrayDijkstra.dijkstra(graph, source, is_matrix)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        total_time += end_time - start_time
        total_memory += peak

    return final_distances, total_time / TRIALS, total_memory / TRIALS


def run_heap_average(graph, source):
    # Averaging the heap version over 5 runs
    total_time = 0
    total_memory = 0
    final_distances = None

    for _ in range(TRIALS):
        tracemalloc.start()
        start_time = time.perf_counter()

        final_distances = MinHeap.dijkstra_heap(graph, source)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        total_time += end_time - start_time
        total_memory += peak

    return final_distances, total_time / TRIALS, total_memory / TRIALS


def print_distances(distances, use_letters):
    # This prints the shortest distances
    for i in range(len(distances)):
        if use_letters:
            node_name = chr(ord("A") + i)
        else:
            node_name = i + 1

        print(f"Node: {node_name}  Shortest Path: {distances[i]}")


def main():
    graphs = [
        {
            "name": "Sparse Graph 1",
            "type": "Sparse",
            "array_graph": ArrayDijkstra.sparseA,
            "heap_graph": ArrayDijkstra.sparseA,
            "source": 0,
            "is_matrix": False,
            "use_letters": True
        },
        {
            "name": "Sparse Graph 2",
            "type": "Sparse",
            "array_graph": ArrayDijkstra.sparseb,
            "heap_graph": ArrayDijkstra.sparseb,
            "source": 0,
            "is_matrix": False,
            "use_letters": False
        },
        {
            "name": "Dense Graph 1",
            "type": "Dense",
            "array_graph": ArrayDijkstra.densea,
            "heap_graph": MinHeap.matrix_to_list(ArrayDijkstra.densea),
            "source": 0,
            "is_matrix": True,
            "use_letters": True
        },
        {
            "name": "Dense Graph 2",
            "type": "Dense",
            "array_graph": ArrayDijkstra.denseb,
            "heap_graph": MinHeap.matrix_to_list(ArrayDijkstra.denseb),
            "source": 0,
            "is_matrix": True,
            "use_letters": False
        },
        {
            "name": "Dense Graph 3",
            "type": "Dense",
            "array_graph": ArrayDijkstra.dense3,
            "heap_graph": MinHeap.matrix_to_list(ArrayDijkstra.dense3),
            "source": 0,
            "is_matrix": True,
            "use_letters": False
        }
    ]

    print("Project 2 Final Results")
    print(f"Each runtime and memory number is averaged over {TRIALS} runs.\n")

    print("=" * 118)
    print(
        f"{'Graph':<18}"
        f"{'Type':<10}"
        f"{'V':<6}"
        f"{'E':<6}"
        f"{'Source':<10}"
        f"{'Array Time':<18}"
        f"{'Heap Time':<18}"
        f"{'Array Mem':<15}"
        f"{'Heap Mem':<15}"
        f"{'Same':<8}"
    )
    print("=" * 118)

    saved_results = []

    for item in graphs:
        name = item["name"]
        graph_type = item["type"]
        array_graph = item["array_graph"]
        heap_graph = item["heap_graph"]
        source = item["source"]
        is_matrix = item["is_matrix"]
        use_letters = item["use_letters"]

        array_distances, array_time, array_memory = run_array_average(
            array_graph,
            source,
            is_matrix
        )

        heap_distances, heap_time, heap_memory = run_heap_average(
            heap_graph,
            source
        )

        same = array_distances == heap_distances

        vertices = len(array_graph)
        edges = count_edges(array_graph, is_matrix)

        if use_letters:
            source_label = chr(ord("A") + source)
        else:
            source_label = source + 1

        saved_results.append(
            {
                "name": name,
                "array_distances": array_distances,
                "heap_distances": heap_distances,
                "use_letters": use_letters,
                "same": same
            }
        )

        print(
            f"{name:<18}"
            f"{graph_type:<10}"
            f"{vertices:<6}"
            f"{edges:<6}"
            f"{str(source_label):<10}"
            f"{array_time:<18.8f}"
            f"{heap_time:<18.8f}"
            f"{array_memory:<15.2f}"
            f"{heap_memory:<15.2f}"
            f"{'Yes' if same else 'No':<8}"
        )

    print("=" * 118)

    print("\nShortest Path Distances\n")

    for result in saved_results:
        print(result["name"])

        print("Array-Based Dijkstra:")
        print_distances(result["array_distances"], result["use_letters"])

        print("Heap-Based Dijkstra:")
        print_distances(result["heap_distances"], result["use_letters"])

        print(f"Same distances: {'Yes' if result['same'] else 'No'}")
        print()


if __name__ == "__main__":
    main()
