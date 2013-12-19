import math

def checkio(inset):
    def sequence_gen():
        r = (1, 1, 1)
        yield r
        while True:
            i, prev_min, prev_max = r
            r = (i+1, prev_max + 1, prev_max + (prev_max - prev_min) + 2)
            yield r

    def build_rows():
        rows = {}
        g = sequence_gen()
        while True:
            i, _min, _max = g.next()
            rows[i] = (_min, _max)
            if i >= 255:
                break
        return rows

    rows = build_rows()

    def get_row(n):
        approx = int(math.sqrt(n * 2))
        if rows.get(approx)[0] <= n <= rows.get(approx)[1]:
            return approx
        elif rows.get(approx)[0] > n:
            return get_row(n - 1)
        else:
            return get_row(n+1)

    return map(get_row, inset)

if __name__ == "__main__":
    print checkio([7, 10, 25])
