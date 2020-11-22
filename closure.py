""" Showcase utility of higher order functions, closure and decorator """


def memoize(func):
    results = {}

    def inner(*args, debug=False):
        if debug:
            print(args)
        try:
            return results[args]
        except KeyError:
            if debug:
                print("Computing new result!")
            results[args] = func(*args)
        return results[args]

    return inner


add = lambda x, y: x + y
product = lambda x, y: x * y

memoized_add = memoize(add)
memoized_product = memoize(product)

print(memoized_add(2, 3))
print(memoized_add(2, 3))

print(memoized_product(2, 3))
print(memoized_product(2, 3))

memoized_fib = None


@memoize
def fib(n):
    if n <= 1:
        return 1

    return fib(n - 1) + fib(n - 2)


# print([fib(n, debug=True) for n in range(10)])
print([fib(n) for n in range(10)])
