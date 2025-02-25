import time


def timer_wrapper(func):
    def wrapper(counter):
        start_time = time.perf_counter()
        result = func(counter)
        end_time = time.perf_counter()
        print(f"Час виконання: {end_time - start_time:.8f} секунд")
        return result
    return wrapper


@timer_wrapper
def prime_num_getter(counter):
    for i in range(0, counter):
        i += 1
        yield i


n = int(input("Введіть число: "))
generator = prime_num_getter(n)
for i in range(0, n):
    print(next(generator))

