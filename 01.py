def parse():
    with open("01.in") as f:
        return f.readlines()

def main():
    lines = parse()
    res = 0
    pos = 50
    for line in lines:
        direction = 1 if line[0] == 'R' else -1
        pos += direction * int(line[1:])

        # do mod
        pos %= 100
        if pos == 0:
            res += 1
    print(res)

    pos = 50
    res = 0
    for line in lines:
        direction = 1 if line[0] == 'R' else -1
        dist = int(line[1:])

        if pos == 0:
            res += abs(dist) // 100
            pos += direction * int(line[1:])
            pos %= 100
        else:
            pos += direction * int(line[1:])
            res += abs(pos // 100)
            pos %= 100
            if pos == 0 and direction == -1:
                res += 1
        
    print(res)
    

if __name__ == "__main__":
    main()
