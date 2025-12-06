def parse():
    with open("03.in") as f:
        lines = f.readlines()
        res = [list(map(int, line.strip())) for line in lines]
        return res

def main():
    all_bats = parse()
    res = 0
    for bats in all_bats:
        top = [0, 0]
        for i, bat in enumerate(bats):
            if bat > top[0] and i < len(bats) - 1:
                top[0] = bat
                top[1] = 0
            elif bat >= top[1]:
                top[1] = bat
        res += top[0] * 10 + top[1]
    print("Part 1", res)

    res = 0
    for bats in all_bats:
        top = [0] * 12
        for i, bat in enumerate(bats):
            for j in range(12):
                if bat > top[j] and i < len(bats) - 11 + j:
                    top[j] = bat
                    for k in range(j + 1, 12):
                        top[k] = 0
                    break
        res += sum(top[i] * 10**(11 - i) for i in range(12))
    print("Part 2", res)

if __name__ == "__main__":
    main()
