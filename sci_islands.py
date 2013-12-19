from collections import defaultdict

def print_replaces(replaces):
    for k in sorted(replaces.keys()):
        print "%d: %d %s" % (k, replaces[k][0], sorted(replaces[k][1]))

def checkio(data):
    def get_value(x,y):
        if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
            return 0
        else:
            return data[y][x]
    curr = 1
    replaces = defaultdict(lambda: [0, set()])
    for y in range(len(data)):
        for x in range(len(data[y])):
            if get_value(x, y) > 0:
                if get_value(x - 1, y) == 0:
                    curr += 1
                replaces[curr][0] += 1
                data[y][x] = curr
                for dx in [-1, 0, 1]:
                    v = get_value(x + dx, y - 1)
                    if v > 0:
                        replaces[curr][1].add(v)
    for i in reversed(sorted(replaces.keys())):
        sq, upper = replaces[i][0], sorted(replaces[i][1])
        if len(upper) > 0:
            top = upper[0]
            replaces[top][0] += sq
            replaces[i][0] = 0
            for j in upper[1:]:
                replaces[j][1].add(top)
    return sorted([i for i in map(lambda x: x[0], replaces.values()) if i > 0])
    

if __name__ == "__main__":
    print checkio([[1, 0, 1, 0, 1],
                   [0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 0],
                   [1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1]])
