from collections import deque

def parse():
    res = []
    with open("10.in") as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            items = line.split()
            goal_str = items[0]
            jolt_str = items[-1]
            btn_strs = items[1:-1]
            n = len(goal_str) - 2

            goal = 0
            for i in range(1, len(goal_str) - 1):
                if goal_str[i] == "#":
                    goal |= 1 << (i - 1)


            jolt_fmt = tuple(map(int, jolt_str[1:-1].split(",")))

            btns = []
            for btn_str in btn_strs:
                btn = 0
                for i in map(int, btn_str[1:-1].split(",")):
                    btn |= 1 << i
                btns.append(btn)

            res.append({
                "n": n,
                "goal": goal,
                "btns": btns,
                "jolts": jolt_fmt,
            })
    return res

def parse2():
    res = []
    with open("10.in") as f:
        lines = [line.strip() for line in f.readlines()]
    for line in lines:
        items = line.split()
        btns_str = items[1:-1]
        jolt_str = items[-1]

        btns = []
        for btn_str in btns_str:
            btn = tuple(map(int, btn_str[1:-1].split(",")))
            btns.append(btn)
        
        jolt = list(map(int, jolt_str[1:-1].split(",")))
        n = len(jolt)

        res.append({
            "n": n,
            "btns": btns,
            "jolt": jolt
        })
    return res
        

def find_fewest_presses1(n, goal, btns):
    # first, build state space. n should be small enough
    graph = {}
    for node in range(2 ** n):
        graph[node] = [node ^ btn for btn in btns]
    
    # do a bfs
    queue = deque([0])
    seen = {0}

    level = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            cur = queue.popleft()
            if cur == goal:
                return level
            for nxt in graph[cur]:
                if nxt not in seen:
                    queue.append(nxt)
                    seen.add(nxt)
        level += 1
    return -1

def find_fewest_presses2(n, goal, btns):
    queue = deque([goal])
    seen = {tuple(goal)}

    level = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            cur = queue.popleft()
            if sum(cur) == 0:
                return level
            for btn in btns:
                nxt = list(cur)
                for i in btn:
                    nxt[i] -= 1
                    if nxt[i] < 0:
                        break
                else:
                    if tuple(nxt) not in seen:
                        queue.append(nxt)
                        seen.add(tuple(nxt))
        level += 1
    return -1

    

def main():
    infos = parse()
    
    res = 0
    for info in infos:
        res += find_fewest_presses1(info["n"], info["goal"], info["btns"])
    print("Part 1", res)

    infos = parse2()
    res = 0
    for i, info in enumerate(infos):
        print(i)
        res += find_fewest_presses2(info["n"], info["jolt"], info["btns"])
    print("Part 2", res)
        

if __name__ == "__main__":
    main()
