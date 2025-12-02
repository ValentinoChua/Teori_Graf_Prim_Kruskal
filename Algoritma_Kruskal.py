# Struktur Union-Find (Disjoint Set)
class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

# Daftar sisi (edge list) dari graf
edges = [
    ('a', 'b', 2),
    ('a', 'c', 1),
    ('b', 'c', 3),
    ('b', 'd', 5),
    ('c', 'd', 3),
    ('c', 'e', 6),
    ('d', 'e', 8),
    ('d', 'f', 4),
    ('e', 'f', 1)
]

# Fungsi Kruskal
def kruskal_mst(vertices, edges):
    uf = UnionFind(vertices)
    mst = []

    # Urutkan sisi berdasarkan bobot
    sorted_edges = sorted(edges, key=lambda x: x[2])

    for u, v, weight in sorted_edges:
        if uf.union(u, v):
            mst.append((u, v, weight))

    return mst

# Contoh pemanggilan
vertices = ['a', 'b', 'c', 'd', 'e', 'f']
mst_result = kruskal_mst(vertices, edges)

# Cetak hasil MST
for edge in mst_result:
    print(f"{edge[0]} — {edge[1]} ({edge[2]})")