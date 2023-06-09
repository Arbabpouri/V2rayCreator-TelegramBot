from itertools import chain

a = [
    [123, 456, 789],
    [987, 654, 321],
    [111, 222, 333],
    [444, 555, 666],
    [777, 888, 999]
]
aa = chain.from_iterable(a)
print(list(aa))