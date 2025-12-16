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

    # for part 2, O(n^2) compare all possible rectangles
    # when considering a rectangle, make sure that _all_ points stay outside of the rectangle and don't cross it
    def check(i, j):
        p1 = pts[i]
        p2 = pts[j]

        # bounds
        i1 = min(p1[0], p2[0])
        i2 = max(p1[0], p2[0])
        j1 = min(p1[1], p2[1])
        j2 = max(p1[1], p2[1])

        for k in range(len(pts)):
            ii, jj = pts[k]

            # point lies inside
            if i1 < ii < i2 or j1 < jj < j2:
                return False
            
            prev_i, prev_j = pts[(k - 1) % len(pts)]
            # point travels across
            if i1 < ii < i2:
                if min(prev_j, jj) < j1 and max(prev_j, jj) > j2:
                    return False
            if j1 < jj < j2:
                if min(prev_i, ii) < i1 and max(prev_i, ii) > i2:
                    return False
        return True

    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if check(i, j):
                res = max(res, get_area(pts[i], pts[j]))
                print(pts[i], pts[j], res)
    print("Part 2", res)

if __name__ == "__main__":
    main()
