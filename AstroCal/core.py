
def run():
    hello()
    fib(20)

def hello():
    print("Hello, moon!")

def fib(n):
    print(str(1))
    next_fib(1, 0, 1, n)


def next_fib(current, previous, i, limit):
    i += 1
    next = (current + previous)
    print(str(next))
    if (i < limit):
        next_fib(next, current, i, limit)

"""My first PR!"""