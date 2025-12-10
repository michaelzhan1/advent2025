from functools import reduce

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def dist_sq(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # return if a union actually happened
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1
            
            return True
        return False

def parse():
    with open("08.in") as f:
        lines = f.readlines()
        points = [Point(*map(int, line.strip().split(","))) for line in lines]
        return points

def main():
    points = parse()
    n = len(points)
    
    dists = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1 = points[i]
            p2 = points[j]
            dist = p1.dist_sq(p2)

            dists.append((dist, i, j))
    dists.sort()

    uf = UF(n)
    num_connections = 1000
    for k in range(num_connections):
        _, i, j = dists[k]
        uf.union(i, j)
    
    circuits = {}
    for i in range(n):
        root = uf.find(i)
        if root not in circuits:
            circuits[root] = 0
        circuits[root] += 1
    
    values = sorted(circuits.values(), reverse=True)
    res = values[0] * values[1] * values[2]
    print("Part 1", res)

    uf = UF(n)
    last_pts = [None, None]
    for _, i, j in dists:
        did_union = uf.union(i, j)
        if did_union:
            last_pts = [points[i], points[j]]
    res = last_pts[0].x * last_pts[1].x
    print("Part 2", res)


if __name__ == "__main__":
    main()
