from bisect import bisect_left

def parse():
    with open("05.in") as f:
        all_lines = f.read()
        fresh_raw, q_raw = all_lines.split("\n\n")
        fresh = []
        for fr in fresh_raw.split("\n"):
            temp = fr.strip().split("-")
            fresh.append(list(map(int, temp)))
        
        qs = list(map(int, q_raw.split("\n")))
        return fresh, qs

def query(ranges, x):
    q = [x, float('inf')] # always prefer to come after the valid range
    i = bisect_left(ranges, q)
    return i > 0 and x <= ranges[i - 1][1] 

def main():
    fs, qs = parse()
    
    fs.sort()
    merged = [list(fs[0])]
    for i in range(1, len(fs)):
        start, end = fs[i]
        # overlaps
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    res = 0
    for q in qs:
        if query(merged, q):
            res += 1
    print("Part 1", res)

    res = 0
    for start, end in merged:
        res += end - start + 1
    print("Part 2", res)

if __name__ == "__main__":
    main()
