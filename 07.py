from collections import defaultdict

def parse():
    with open("07.in") as f:
        lines = f.readlines()
        return [line.strip() for line in lines]

def main():
    lines = parse()
    m = len(lines[0])

    beams = set([lines[0].index("S")])
    splits = []
    for line in lines[1:]:
        found = set([i for i in range(len(line)) if line[i] == "^"])
        if found:
            splits.append(found)
    
    res = 0
    for i in range(len(splits)):
        count = 0
        to_add = set()
        for beam in beams:
            if beam in splits[i]:
                if beam > 0:
                    to_add.add(beam - 1)
                if beam < m - 1:
                    to_add.add(beam + 1)
                count += 1
            else:
                to_add.add(beam)
        
        res += count
        beams = to_add
    print("Part 1", res)

    beams = {lines[0].index("S"): 1}
    for i in range(len(splits)):
        to_add = defaultdict(int)
        for beam, count in beams.items():
            if beam in splits[i]:
                if beam > 0:
                    to_add[beam - 1] += count
                if beam < m - 1:
                    to_add[beam + 1] += count
            else:
                to_add[beam] += count
        beams = to_add
    res = sum(beams.values())
    print("Part 2", res)



if __name__ == "__main__":
    main()
