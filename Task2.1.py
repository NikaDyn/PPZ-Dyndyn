def fibonacci_seq_generator():
    numebers_fib = [1, 1]
    while True:
        result = numebers_fib[0] + numebers_fib[1]
        numebers_fib[0] = numebers_fib[1]
        numebers_fib[1] = result
        yield result


generator = fibonacci_seq_generator()
i = 0
while i < 10:
    print(next(generator))
    i += 1
