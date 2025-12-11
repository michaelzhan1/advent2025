def parse():
    with open("09.in") as f:
        lines = f.readlines()
        return [list(map(int, line.strip().split(","))) for line in lines]

def get_area(p1, p2):
    return abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)

def main():
    pts = parse()
    n = len(pts)
    
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            res = max(res, get_area(pts[i], pts[j]))
    print("Part 1", res)

if __name__ == "__main__":
    main()
