import time
import tracemalloc
import random   

def time_trace(graph,source, isMatrix=False,letters=False):
   tracemalloc.start()
   start_time = time.perf_counter()
   comp=dijkstra(graph,source,isMatrix)
   end_time=time.perf_counter()
   current, peak = tracemalloc.get_traced_memory()
   tracemalloc.stop()
   
   if letters == True:
        temp = ord('A')
        for rows in comp:
            print(f"Node: {chr(temp)}  Shortest Path: {rows}")
            temp+=1
        print(f"Time used: {end_time - start_time:.8f} seconds")
        print(f"Memory: {peak} B\n")
   elif letters == False:
       temp = 1
       for rows in comp:
            print(f"Node: {temp}  Shortest Path: {rows}")
            temp+=1
       print(f"Time used: {end_time - start_time:.8f} seconds")
       print(f"Memory: {peak} B\n")

def dijkstra (graph, source, isMatrix=False):
    Vertices = len(graph)
    distance = [99] * Vertices
    visited = [False] * Vertices
    distance[source]=0

    for i in range(Vertices):
        smallest_dist = 99
        min_dex = -1

        for v in range(Vertices):
            if distance[v]< smallest_dist and not visited[v]:
                smallest_dist = distance[v]
                min_dex = v
        
        if min_dex == -1:
            break        
        
        visited[min_dex]=True

        if isMatrix == False:
            for neighbor , weight in graph[min_dex]:
                if weight > 0 and not visited[neighbor] and distance[min_dex]+weight <distance[neighbor]:
                    distance[neighbor] = distance[min_dex]+weight

        if isMatrix == True:
            for j in range(Vertices):
                weight = graph[min_dex][j]
                if weight > 0 and not visited[j] and distance[min_dex]+weight <distance[j]:
                    distance[j] = distance[min_dex]+weight
    return distance

sparseA = {
    #use letters 
    0:[(1,4),(2,2)],
    1:[(0,4),(3,5)],
    2:[(0,2),(3,1)],
    3:[(1,5),(2,1),(4,3)],
    4:[(3,3),(5,2)],
    5:[(4,2)]
}
sparseb = {
    0:[(1,3),(2,6)],
    1:[(0,3),(3,2),(4,5)],
    2:[(0,6),(4,4)],
    3:[(1,2),(5,7)],
    4:[(1,5),(2,4),(6,1)],
    5:[(3,7)],
    6:[(4,1)]
}
densea = [
    [0,2,5,1,4],
    [2,0,3,2,6],
    [5,3,0,3,1],
    [1,2,3,0,2],
    [4,6,1,2,0]
]
denseb = [
    [0,3,2,6,5,4],
    [3,0,1,2,4,7],
    [2,1,0,3,6,5],
    [6,2,3,0,2,4],
    [5,4,5,2,0,1],
    [4,7,6,4,1,0]
]
n=10
dense3=[[0 for _ in range(n)] for _ in range (n)]
for i in range(n):
    dense3[i][i] = 0
    for j in range(i + 1, n):
        val = random.randint(0, 20)
        dense3[i][j] = dense3[j][i] = val


print("Sparese Graph 1:")
time_trace(sparseA,0,False,True)
print("Sparese Graph 2:")
time_trace(sparseb,0)
print("Dense Graph 1:")
time_trace(densea,0,True,True)
print("Dense Graph 2:")
time_trace(denseb,0,True)
print("Dense Graph 3:")
print("Generated Graph")
for row in dense3:
    print(row)
time_trace(dense3,0,True)