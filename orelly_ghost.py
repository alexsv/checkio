def checkio(opacity):
    def fib_generator():
        prev, curr = 0, 1
        while True:
            prev, curr = curr, prev+curr
            yield curr
            
    fib = fib_generator()
    fib_numbers = set([fib.next() for i in range(19)])
    
    result = {10000: 0}
    curr_opacity = 10000
    for i in range(1, 5000):
        curr_opacity -= i if i in fib_numbers else -1
        result[curr_opacity] = i
    return result[opacity]

if __name__ == "__main__":
    print checkio(9989)