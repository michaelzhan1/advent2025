from functools import reduce

def parse():
    with open("06.in") as f:
        lines = f.readlines()
        res = []
        for line in lines[:-1]:
            res.append([int(x) for x in line.strip().split(' ') if x])
        
        ops = [line for line in lines[-1].strip().split(' ') if line]
        return res, ops

def parse2():
    with open("06.in") as f:
        lines = f.readlines()
        temp = [line[:-1] for line in lines]
        nums = temp[:-1]
        ops = temp[-1]

        i = 0
        gaps = []
        gap = 0
        for i in range(len(ops)):
            if ops[i] == ' ':
                if ops[i - 1] == ' ':
                    gap += 1
                else:
                    gap = 0
            else:
                if i > 0:
                    gaps.append(gap + 1)
        gaps.append(gap + 2)
        return nums, ops, gaps


def main():
    lines, ops = parse()
    
    n = len(lines)
    m = len(lines[0])

    res = 0
    for j in range(m):
        op = (lambda a, b: a * b) if ops[j] == '*' else (lambda a, b: a + b)
        initial = 1 if ops[j] == '*' else 0
        xs = [lines[i][j] for i in range(n)]
        res += reduce(lambda x, y: op(x, y), xs, initial)
    print("Part 1", res)

    res = 0
    lines, ops, digits = parse2()

    di = 0
    j = 0
    while j < len(lines[0]):
        start_j = j
        op = (lambda a, b: a * b) if ops[start_j] == '*' else (lambda a, b: a + b)
        initial = 1 if ops[start_j] == '*' else 0

        nums = []
        while j < start_j + digits[di]:
            num = 0
            for line in lines:
                if line[j] == ' ':
                    continue
                
                num *= 10
                num += int(line[j])
            nums.append(num)
            j += 1

        temp = reduce(lambda x, y: op(x, y), nums, initial)
        res += temp
        
        di += 1
        j += 1 # account for space
    print("Part 2", res)

if __name__ == "__main__":
    main()
