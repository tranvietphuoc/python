# this is a closure
def outer():
    x = 1

    def inner():
        nonlocal x
        print(f"x before change {x}")
        x += 1
        print(f"x after change {x}")

    return inner


f = outer()

for i in range(5):
    print(f"Run {i+1}")
    f()
    print("\n")


# make a fibonacci with closure
# now we can replace recursive function or dynamic planning by closure
def fib():
    x_0 = 0
    x_1 = 1

    def get_next_fib_num():
        nonlocal x_0, x_1
        x_2 = x_0 + x_1
        x_0, x_1 = x_1, x_2
        return x_2

    return get_next_fib_num


fibonacci = fib()
for i in range(2, 21):
    num = fibonacci()
    print(f"The {i}th fibonacci number is {num}")
