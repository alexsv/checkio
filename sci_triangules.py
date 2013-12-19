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

    def solve_3(inset):
        a, b, c = sorted(inset)
        ra, rb, rc = map(get_row, [a, b, c])
        if ra == rb or rb == rc and ra != rc:
            if ra == rb
                width, height = b - a, rc - rb
            elif b == c:
                width, height = c - a, rb - a
            if width == height and width > 0:
                return 3
        return 0

    def solve_4(inset):
        return 0

    def solve_6(inset):
        a, b, c, d, e, f = sorted(inset)
        ab, cd, ef = b - a, f - c, f - e
        ra, rb, rc, rd, re, rf = map(get_row, [a, b, c, d, e, f])

        if ra == rb and rc == rd and re == rf
           and ra < rc < rf and ab > 0
           and ef == ab and cd == 2 * ab
           and c - a == ra:
            return 6
        else:
            return 0

    return map(get_row, inset)

if __name__ == "__main__":
    print checkio([7, 10, 25])
