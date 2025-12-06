from collections import deque

def parse():
    with open("04.in") as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]

def main():
    arr = parse()
    n = len(arr)
    m = len(arr[0])
    
    res = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '.':
                continue

            count = 0
            for ii in range(max(0, i - 1), min(n, i + 2)):
                for jj in range(max(0, j - 1), min(m, j + 2)):
                    if arr[ii][jj] == '@':
                        count += 1
            
            if count <= 4: # count includes the cell itself
                res += 1
    print("Part 1", res)

    res = 0

    # build queue
    queue = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '.':
                continue
            
            count = 0
            for ii in range(max(0, i - 1), min(n, i + 2)):
                for jj in range(max(0, j - 1), min(m, j + 2)):
                    if arr[ii][jj] == '@':
                        count += 1
            
            if count <= 4:
                queue.append((i, j))

    
    # bfs down 
    while queue:
        # remove items
        res += len(queue)
        for i, j in queue:
            arr[i][j] = '.'
        
        # look at neighbors
        seen = set()
        size = len(queue)
        for _ in range(size):
            i, j = queue.popleft()

            for ii in range(max(0, i - 1), min(n, i + 2)):
                for jj in range(max(0, j - 1), min(m, j + 2)):
                    if ii == i and jj == j or arr[ii][jj] == '.':
                        continue
                    
                    count = 0
                    for iii in range(max(0, ii - 1), min(n, ii + 2)):
                        for jjj in range(max(0, jj - 1), min(m, jj + 2)):
                            if arr[iii][jjj] == '@':
                                count += 1
                    
                    if count <= 4 and (ii, jj) not in seen:
                        queue.append((ii, jj))
                        seen.add((ii, jj))
    print("Part 2", res)


if __name__ == "__main__":
    main()
