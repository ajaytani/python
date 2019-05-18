dict = {}


def fibonacci(n):
    # Write your code here.
    if n == 0 or n == 1:
        return n
    if n in dict:
        return dict[n]

    dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dict[n]


n = 5
print(fibonacci(n))


def genfib():

    pp, p = 0,1

    while 1:
        yield pp
        pp, p = p, pp+p

g = genfib()
for i in range(n):
    print(next(g))