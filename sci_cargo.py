
def checkio(data):
    _min = sum(data)
    for i in range(1, 2 ** len(data)):
        sum_a, sum_b = 0, 0
        for v, sign in zip(data, bin(i)[2:].zfill(len(data))):
            if sign == '0':
                sum_a += v
            else:
                sum_b += v
        if abs(sum_a - sum_b) < _min:
            _min = abs(sum_a - sum_b)
    return _min

if __name__ == "__main__":
    print checkio([5, 8, 13, 27, 14])
