import heapq

# Representasi graf sebagai adjacency list
graph = {
    'a': [('b', 1), ('c', 7)],
    'b': [('a', 1), ('c', 5), ('e', 4), ('d', 3)],
    'c': [('a', 7), ('b', 5), ('d', 1)],
    'd': [('b', 3), ('c', 1), ('e', 2), ('h', 3), ('i', 3)],
    'e': [('b', 4), ('d', 2), ('f', 1), ('h', 4)],
    'f': [('e', 1), ('g', 2)],
    'g': [('f', 2), ('h', 8)],
    'h': [('e', 4), ('d', 3), ('g', 8), ('j', 7)],
    'i': [('d', 3), ('j', 4)],
    'j': [('i', 4), ('h', 7)]
}

def prim_mst(start):
    visited = set()
    mst = []
    min_heap = []

    # Masukkan semua sisi dari simpul awal ke heap
    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))

    while min_heap:
        weight, frm, to = heapq.heappop(min_heap)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            for neighbor, w in graph[to]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, to, neighbor))

    return mst

# Contoh pemanggilan
mst_result = prim_mst('a')
for edge in mst_result:
    print(f"{edge[0]} — {edge[1]} ({edge[2]})")