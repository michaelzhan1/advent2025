def parse():
    with open("02.in") as f:
        line = f.read().strip()
        ids = list(map(lambda x: list(map(int, x.split("-"))), line.split(",")))
        return ids

def main():
    ids = parse()
    res = 0
    for i1, i2 in ids:
        for i in range(i1, i2 + 1):
            s = str(i)
            if len(s) % 2 == 0:
                n = len(s)
                if s[:n // 2] == s[n // 2:]:
                    res += i
    print("Part 1", res)

    res = 0
    for i1, i2 in ids:
        for i in range(i1, i2 + 1):
            s = str(i)
            n = len(s)
            for numparts in range(2, n + 1):
                if n % numparts != 0:
                    continue

                if s == (s[:n // numparts] * numparts):
                    res += i
                    break
    print("Part 2", res)

if __name__ == "__main__":
    main()
