from functools import cache

def parse():
    graph = {}
    with open("11.in") as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            a, b = line.split(":")
            graph[a] = b.strip().split()
    return graph

def count_paths(graph):
    @cache
    def dfs(cur):
        if cur == "out":
            return 1
        res = 0
        for nxt in graph.get(cur, []):
            res += dfs(nxt)
        return res
    return dfs("you")

def count_paths2(graph):
    @cache
    def dfs(cur, dac, fft):
        if cur == "out":
            return 1 if dac and fft else 0
        res = 0
        for nxt in graph.get(cur, []):
            res += dfs(nxt, dac or nxt == "dac", fft or nxt == "fft")
        return res
    return dfs("svr", False, False)

def main():
    graph = parse()
    res = count_paths(graph)
    print("Part 1", res)

    res = count_paths2(graph)
    print("Part 2", res)

if __name__ == "__main__":
    main()
